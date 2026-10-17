"""Check the tracked public package without downloading participant data."""

import ast
import csv
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DATA = {"data/README.md", "data/download_manifest.csv"}
REQUIRED = {
    ".gitignore", "AGENTS.md", "README.md", *PUBLIC_DATA,
    "docs/00_INDEX.md", "docs/03_REFINED_PROPOSAL.md",
    "docs/05_TEAM_DECISIONS.md", "docs/06_SCIENTIFIC_DEVELOPMENT_PLAN.md",
    "docs/07_COLLABORATION_GUIDE.md", "scripts/verify_repository.py",
}


def tracked_files():
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True)
    return {Path(p.decode()) for p in result.stdout.split(b"\0") if p}


def check_links(root, paths):
    """Validate local Markdown links against the published file set."""
    allowed = {p.resolve() for p in paths}
    errors = []
    checked = 0
    for document in sorted(paths):
        if document.suffix != ".md" or not document.is_file():
            continue
        body = document.read_text(encoding="utf-8")
        for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", body):
            target = match.group(1).strip().strip("<>")
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            checked += 1
            resolved = (document.parent / target).resolve()
            if resolved not in allowed or not resolved.is_file():
                errors.append(f"Unpublished/broken link: {document.relative_to(root)} -> {target}")
    return checked, errors


def main():
    try:
        relative = tracked_files()
    except subprocess.CalledProcessError:
        raise SystemExit("Run inside a Git checkout; stage the intended public files first.")
    names = {p.as_posix() for p in relative}
    errors = [f"Required file not tracked: {p}" for p in sorted(REQUIRED - names)]
    paths = {ROOT / p for p in relative}
    for path in sorted(relative):
        name = path.as_posix()
        parts = path.parts
        if (parts[0] == "data" and name not in PUBLIC_DATA
                or parts[0] in {".aws", ".agents", ".codex", ".venv", "outputs", "results", "checkpoints"}
                or "__pycache__" in parts or ".ipynb_checkpoints" in parts
                or path.name.startswith(".env")
                or path.suffix in {".pyc", ".pem", ".key", ".part"}):
            errors.append(f"Excluded local artifact tracked: {name}")
        source = ROOT / path
        if not source.is_file() or source.is_symlink():
            errors.append(f"Missing file or unsupported symlink: {name}")
            continue
        if path.suffix == ".py":
            try:
                ast.parse(source.read_text(encoding="utf-8"), filename=name)
            except SyntaxError as exc:
                errors.append(f"Python syntax: {name}: {exc}")
        if path.suffix == ".ipynb":
            notebook = json.loads(source.read_text(encoding="utf-8"))
            if any(c.get("outputs") or c.get("execution_count") is not None
                   for c in notebook.get("cells", []) if c.get("cell_type") == "code"):
                errors.append(f"Notebook has saved execution output: {name}")
        if path.suffix in {".md", ".py", ".csv", ".json", ".ipynb"}:
            body = source.read_text(encoding="utf-8-sig")
            if re.search(r"(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----)", body):
                errors.append(f"Possible credential in: {name}")
            if "docs/" + "presentation" in body or "00_PRESENTATION" + "_BRIEF.md" in body:
                errors.append(f"Retired presentation reference: {name}")

    checked, link_errors = check_links(ROOT, paths)
    errors.extend(link_errors)
    manifest_path = ROOT / "data/download_manifest.csv"
    if manifest_path.is_file():
        with manifest_path.open(newline="", encoding="utf-8") as stream:
            records = list(csv.DictReader(stream))
        if len(records) != len({r["path"] for r in records}):
            errors.append("Duplicate manifest paths")
        for row in records:
            if (row["status"] not in {"downloaded", "local"}
                    or not re.fullmatch(r"[0-9a-f]{64}", row["sha256"])
                    or not row["bytes"].isdigit()):
                errors.append(f"Invalid reference manifest record: {row['path']}")
    result = {"tracked_files": len(names), "local_links_checked": checked,
              "source_data_required": False, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
