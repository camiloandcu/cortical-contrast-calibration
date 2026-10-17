"""Create descriptive inventories from downloaded files; no research models are fitted."""

import csv
import json
import math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw"
OUT = ROOT / "data/derived"
MISSING = {"", "NA", "NaN", "nan", "N/A", "-9999", "-9999.0"}


def write_csv(path, rows, fields=None):
    if not rows and fields is None:
        return
    with path.open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields or list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def load_table(path):
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream, delimiter="\t" if path.suffix == ".tsv" else ",")
        return reader.fieldnames, list(reader)


def inventory(dataset, fields, rows):
    columns = []
    for i, field in enumerate(fields):
        values = [r[field].strip() for r in rows]
        present = [v for v in values if v not in MISSING]
        numbers = []
        for value in present:
            try:
                number = float(value)
                if not math.isfinite(number):
                    raise ValueError(value)
                numbers.append(number)
            except ValueError:
                break
        numeric = bool(present) and len(numbers) == len(present)
        kind = "integer" if numeric and all(v.is_integer() for v in numbers) else "numeric" if numeric else "text"
        counts = Counter(present)
        columns.append({
            "dataset": dataset, "position": i + 1, "column": field or "<empty_header>",
            "inferred_type": kind, "rows": len(rows),
            "blank_count": values.count(""),
            "missing_or_sentinel_count": len(values) - len(present),
            "missing_percent": round(100 * (len(values) - len(present)) / len(rows), 2),
            "unique_present": len(counts),
            "minimum": min(numbers) if numeric else "", "maximum": max(numbers) if numeric else "",
            "examples": json.dumps(counts.most_common(3), ensure_ascii=False),
        })
    return columns


def group_rows(rows, columns):
    counts = Counter(tuple(r[c] for c in columns) for r in rows)
    return [dict(zip(columns, key), n=count) for key, count in sorted(counts.items())]


def common_support(cohorts):
    """Record descriptive min-max intersections, not inferential positivity."""
    records = []
    for cohort, rows in cohorts.items():
        for site in sorted({r["SITE_ID"] for r in rows}):
            subset = [r for r in rows if r["SITE_ID"] == site]
            entry = {"cohort": cohort, "SITE_ID": site, "n": len(subset)}
            bounds = []
            for diagnosis, sex in [("1", "1"), ("1", "2"), ("2", "1"), ("2", "2")]:
                ages = [float(r["AGE_AT_SCAN"]) for r in subset
                        if (r["DX_GROUP"], r["SEX"]) == (diagnosis, sex)]
                prefix = f"dx{diagnosis}_sex{sex}"
                entry.update({prefix + "_n": len(ages),
                              prefix + "_min_age": min(ages) if ages else "",
                              prefix + "_max_age": max(ages) if ages else ""})
                if ages:
                    bounds.append((min(ages), max(ages)))
            present = len(bounds) == 4
            low = max(x[0] for x in bounds) if present else ""
            high = min(x[1] for x in bounds) if present else ""
            entry.update(all_four_groups_present=int(present),
                         four_group_age_intersection_low=low,
                         four_group_age_intersection_high=high,
                         positive_age_intersection=int(present and high > low))
            records.append(entry)
    write_csv(OUT / "abide1_common_support_by_site.csv", records)


def profile_freesurfer(phenotypes):
    result = []
    roi_rows = []
    reference_regions = set()
    for path in (RAW / "abide1/freesurfer").glob("*/*.stats"):
        reference_regions.update(line.split()[0] for line in path.read_text().splitlines()
                                 if line.strip() and not line.startswith("#"))
    if reference_regions:
        assert len(reference_regions) == 34, "Unexpected atlas; inspect region names"
    roi_fields = [f"{hemi}_{region}_thickness_mm" for hemi in ["lh", "rh"]
                  for region in sorted(reference_regions)]
    raw_stats = []
    for participant in phenotypes:
        fid = participant["FILE_ID"]
        hemispheres = {}
        for hemi in ["lh", "rh"]:
            path = RAW / "abide1/freesurfer" / fid / (hemi + ".aparc.stats")
            if not path.exists():
                continue
            lines = path.read_text().splitlines()
            columns = next(line.split()[2:] for line in lines if line.startswith("# ColHeaders"))
            regions = [dict(zip(columns, line.split())) for line in lines if line and not line.startswith("#")]
            assert len({r["StructName"] for r in regions}) == len(regions)
            assert {r["StructName"] for r in regions} <= reference_regions
            assert "ThickAvg" in columns
            raw_stats.extend(regions)
            hemispheres[hemi] = regions
        observed = {f"{hemi}_{r['StructName']}_thickness_mm": r["ThickAvg"]
                    for hemi, regions in hemispheres.items() for r in regions}
        entry = {"SUB_ID": participant["SUB_ID"], "FILE_ID": fid,
                 "SITE_ID": participant["SITE_ID"], "DX_GROUP": participant["DX_GROUP"],
                 "SEX": participant["SEX"], "AGE_AT_SCAN": participant["AGE_AT_SCAN"],
                 "both_hemispheres": int(len(hemispheres) == 2),
                 "n_regions_available": len(observed),
                 "complete_68_regions": int(len(observed) == 68),
                 "invalid_thickness_values": sum(not math.isfinite(float(v)) or float(v) <= 0
                                                   for v in observed.values()),
                 "qc_anat_rater_2": participant["qc_anat_rater_2"],
                 "qc_anat_rater_3": participant["qc_anat_rater_3"]}
        result.append(entry)
        if len(hemispheres) == 2:
            roi_rows.append(dict(entry, **{field: observed.get(field, "") for field in roi_fields}))
    write_csv(OUT / "abide1_freesurfer_availability.csv", result)
    if roi_rows:
        write_csv(OUT / "abide1_freesurfer_thickness.csv", roi_rows)
    complete = [r for r in result if r["both_hemispheres"]]
    complete_rois = [r for r in complete if r["complete_68_regions"] and not r["invalid_thickness_values"]]
    strict = [r for r in complete_rois if r["qc_anat_rater_2"] == "OK" and r["qc_anat_rater_3"] == "OK"]
    common_support({"bilateral": complete, "complete_68": complete_rois,
                    "illustrative_qc": strict})
    write_csv(OUT / "abide1_site_sex_diagnosis.csv", group_rows(complete, ["SITE_ID", "DX_GROUP", "SEX"]))
    age_bins = []
    for r in complete:
        age = float(r["AGE_AT_SCAN"])
        age_bins.append(dict(r, age_bin="6-11" if age < 12 else "12-17" if age < 18 else "18+"))
    write_csv(OUT / "abide1_age_sex_diagnosis.csv", group_rows(age_bins, ["age_bin", "DX_GROUP", "SEX"]))
    if raw_stats:
        write_csv(OUT / "freesurfer_stats_column_inventory.csv",
                  inventory("abide1/freesurfer_stats", list(raw_stats[0]), raw_stats))
    return {"both_hemispheres": len(complete), "groups": group_rows(complete, ["DX_GROUP", "SEX"]),
            "complete_68_positive_finite_regions": len(complete_rois),
            "complete_68_groups": group_rows(complete_rois, ["DX_GROUP", "SEX"]),
            "incomplete_regions_participants": [r["FILE_ID"] for r in complete if not r["complete_68_regions"]],
            "illustrative_strict_qc_n": len(strict),
            "illustrative_strict_qc_groups": group_rows(strict, ["DX_GROUP", "SEX"]),
            "roi_columns": 68 if complete else 0,
            "qc_note": "Illustrative sensitivity filter, not a validated inclusion rule for FreeSurfer"}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    columns = []
    summary = {}
    fields, phenotypes = load_table(RAW / "abide1/phenotypic.csv")
    columns.extend(inventory("abide1/phenotypic", fields, phenotypes))
    summary["abide1"] = {"rows": len(phenotypes), "columns": len(fields),
                         "age_min": min(float(r["AGE_AT_SCAN"]) for r in phenotypes),
                         "age_max": max(float(r["AGE_AT_SCAN"]) for r in phenotypes),
                         "site_labels": len({r["SITE_ID"] for r in phenotypes}),
                         "no_filename": sum(r["FILE_ID"] == "no_filename" for r in phenotypes),
                         "groups": group_rows(phenotypes, ["DX_GROUP", "SEX"]),
                         "freesurfer": profile_freesurfer(phenotypes)}
    thickness = OUT / "abide1_freesurfer_thickness.csv"
    if thickness.exists():
        fields, rows = load_table(thickness)
        columns.extend(inventory("abide1/freesurfer_thickness_derived", fields, rows))
    write_csv(OUT / "column_inventory.csv", columns)
    (OUT / "audit_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    lines = ["# Inventario de columnas observado", "",
             "Los diez campos originales FreeSurfer se describen en [la revisión](01_DATASET_REVIEW.md) y en el inventario específico (`data/derived/freesurfer_stats_column_inventory.csv`, generado localmente).",
             "La tabla regional derivada conserva el grosor medio, identificadores y campos de auditoría.", "",
             "Generado por `scripts/profile_datasets.py`.", "",
             "Faltantes: vacíos, NA/NaN y -9999. Los tipos se infieren de los valores; no sustituyen el diccionario del repositorio.", ""]
    for ds in dict.fromkeys(c["dataset"] for c in columns):
        lines.extend(["## " + ds, "", "| Columna literal | Tipo observado | Faltantes (%) | Valores únicos | Rango numérico |",
                      "|---|---|---:|---:|---|"])
        for c in columns:
            if c["dataset"] == ds:
                bounds = f"{c['minimum']:g} a {c['maximum']:g}" if c["minimum"] != "" else "—"
                lines.append(f"| `{c['column']}` | {c['inferred_type']} | {c['missing_percent']} | {c['unique_present']} | {bounds} |")
        lines.append("")
    (ROOT / "docs/04_COLUMN_INVENTORY.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"tables": len(summary), "inventoried_columns": len(columns),
                      "abide_freesurfer": summary["abide1"]["freesurfer"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
