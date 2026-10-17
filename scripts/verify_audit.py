"""Verify public-file hashes, descriptive counts and local document links."""

import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def table(relative):
    with (ROOT / relative).open(newline="", encoding="utf-8-sig") as stream:
        return list(csv.DictReader(stream))


def main():
    manifest = table("data/download_manifest.csv")
    assert len({r["path"] for r in manifest}) == len(manifest)
    errors = []
    total_bytes = 0
    for record in manifest:
        path = ROOT / record["path"]
        if record["status"] not in {"downloaded", "local"}:
            errors.append(f"Acquisition status: {record['path']}")
            continue
        if not path.is_file():
            errors.append(f"Missing source: {record['path']}")
            continue
        size = path.stat().st_size
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if size != int(record["bytes"]) or digest != record["sha256"]:
            errors.append(f"Integrity mismatch: {record['path']}")
        total_bytes += size

    phenotypes = table("data/raw/abide1/phenotypic.csv")
    subjects = [r["SUB_ID"] for r in phenotypes]
    files = [r["FILE_ID"] for r in phenotypes if r["FILE_ID"] != "no_filename"]
    unique = len(subjects) == len(set(subjects)) and len(files) == len(set(files))
    assert unique, "Duplicate participant/file identifiers"
    thickness = table("data/derived/abide1_freesurfer_thickness.csv")
    assert len(thickness) == 1035
    complete = [r for r in thickness if r["complete_68_regions"] == "1"
                and r["invalid_thickness_values"] == "0"]
    assert len(complete) == 1027
    summary = json.loads((ROOT / "data/derived/audit_summary.json").read_text())
    assert set(summary) == {"abide1"}
    assert summary["abide1"]["freesurfer"]["both_hemispheres"] == len(thickness)
    assert summary["abide1"]["freesurfer"]["complete_68_positive_finite_regions"] == len(complete)

    broken = []
    checked = 0
    for document in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in document.relative_to(ROOT).parts):
            continue
        for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
            target = match.group(1).strip().strip("<>")
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            checked += 1
            if not (document.parent / target).exists():
                broken.append(f"{document.relative_to(ROOT)} -> {target}")
    errors.extend(broken)
    result = {
        "checked_date": "2026-10-11",
        "verified_at_utc": datetime.now(timezone.utc).isoformat(),
        "download_manifest_entries": len(manifest),
        "unresolved_download_errors": sum(r["status"] not in {"downloaded", "local"} for r in manifest),
        "source_hashes_match": not any("Integrity" in e or "Missing source" in e for e in errors),
        "original_bytes": total_bytes,
        "abide_participants_with_bilateral_files": len(thickness),
        "abide_participants_with_68_positive_finite_regions": len(complete),
        "unique_subject_and_file_ids": unique,
        "local_markdown_links_checked": checked,
        "local_markdown_links_valid": not broken,
        "research_models_fitted": False,
        "scope": "Cortical contrast calibration / ABIDE I",
        "errors": errors,
    }
    (ROOT / "data/derived/verification_summary.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
