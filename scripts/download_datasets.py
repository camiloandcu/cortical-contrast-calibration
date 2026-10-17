"""Download public ABIDE data and optional P5 evidence; no account is used."""

import argparse
import csv
import hashlib
import json
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ABIDE_BASE = "https://fcp-indi.s3.amazonaws.com/data/Projects/ABIDE_Initiative/"


def download(job):
    url, relative = job
    target = ROOT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    record = {"path": relative, "url": url,
              "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "status": "", "bytes": "", "sha256": "", "error": ""}
    for attempt in range(3):
        try:
            if target.exists():
                record["status"] = "local"
            else:
                with urlopen(Request(url, headers={"User-Agent": "DatasetFeasibilityAudit/1.0"}),
                             timeout=45) as response:
                    expected = response.headers.get("Content-Length")
                    with target.with_suffix(target.suffix + ".part").open("wb") as stream:
                        while chunk := response.read(1024 * 1024):
                            stream.write(chunk)
                    partial = target.with_suffix(target.suffix + ".part")
                    if expected and partial.stat().st_size != int(expected):
                        raise ValueError("Incomplete response")
                    partial.replace(target)
                    record["status"] = "downloaded"
            digest = hashlib.sha256()
            with target.open("rb") as stream:
                while chunk := stream.read(1024 * 1024):
                    digest.update(chunk)
            record.update(bytes=target.stat().st_size, sha256=digest.hexdigest())
            return record
        except HTTPError as exc:
            record.update(status=f"http_{exc.code}", error=str(exc))
            if exc.code in (401, 403, 404):
                break
        except Exception as exc:
            record.update(status="error", error=str(exc))
        if attempt < 2:
            time.sleep(attempt + 1)
    return record


def run_jobs(jobs, workers):
    with ThreadPoolExecutor(max_workers=workers) as pool:
        records = list(pool.map(download, jobs))
    print(json.dumps({"jobs": len(records), "success": sum(
        r["status"] in ("downloaded", "local") for r in records)}, ensure_ascii=False), flush=True)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["metadata", "abide-ants", "abide-freesurfer", "p5-evidence"],
                        required=True)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, help="Limit participants, for a pilot only")
    args = parser.parse_args()
    DATA.mkdir(exist_ok=True)
    jobs = []
    if args.mode == "metadata":
        jobs += [
            (ABIDE_BASE + "Phenotypic_V1_0b_preprocessed1.csv",
             "data/raw/abide1/phenotypic.csv"),
            ("https://preprocessed-connectomes-project.github.io/abide/download.html",
             "data/sources/abide_download.html"),
            ("https://preprocessed-connectomes-project.github.io/abide/quality_assessment.html",
             "data/sources/abide_quality_assessment.html"),
            ("http://fcon_1000.projects.nitrc.org/indi/abide/ABIDE_LEGEND_V1.02.pdf",
             "data/sources/ABIDE_LEGEND_V1.02.pdf"),
            ("http://fcon_1000.projects.nitrc.org/indi/abide/ABIDEII_Data_Legend.pdf",
             "data/sources/ABIDEII_Data_Legend.pdf"),
        ]
    elif args.mode == "p5-evidence":
        source = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10412957/"
        jobs = [(source + "fullTextXML", "data/sources/Reynolds2023_fulltext.xml"),
                (source + "supplementaryFiles", "data/sources/Reynolds2023_supplement.zip")]
    else:
        with (DATA / "raw/abide1/phenotypic.csv").open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        file_ids = sorted({r["FILE_ID"] for r in rows if r["FILE_ID"] not in ("", "no_filename")})
        if args.limit:
            file_ids = file_ids[:args.limit]
        for fid in file_ids:
            if args.mode == "abide-ants":
                filename = fid + "_roi_thickness.txt"
                jobs.append((ABIDE_BASE + "Outputs/ants/roi_thickness/" + filename,
                             "data/raw/abide1/ants/" + filename))
            else:
                for hemisphere in ["lh", "rh"]:
                    filename = hemisphere + ".aparc.stats"
                    jobs.append((ABIDE_BASE + "Outputs/freesurfer/5.1/" + fid + "/stats/" + filename,
                                 "data/raw/abide1/freesurfer/" + fid + "/" + filename))
    records = run_jobs(jobs, args.workers)
    manifest = DATA / "download_manifest.csv"
    existing = {}
    if manifest.exists():
        with manifest.open(newline="", encoding="utf-8") as stream:
            existing = {r["path"]: r for r in csv.DictReader(stream)}
    existing.update({r["path"]: r for r in records})
    with manifest.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(existing[k] for k in sorted(existing))
    failures = [r for r in records if r["status"] not in ("downloaded", "local")]
    if failures:
        print(json.dumps({"failures": len(failures), "examples": failures[:3]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
