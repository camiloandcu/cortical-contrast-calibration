# Calibración de contrastes corticales

This project studies interaction estimability and uncertainty after multicenter
cortical-thickness harmonization, calibrated to the observed ABIDE I design.
This file is portable: no personal skills, agent profiles or private setup are
required. Reply in the user's language; use English file conventions and agent
instructions. Do not assume decisions from earlier conversations.

## Authoritative context

- Reading order and evidence: `docs/00_INDEX.md`, `literature/README.md`.
- Scientific design: `docs/03_REFINED_PROPOSAL.md`.
- Independent review and response: `docs/review/02_PEER_REVIEW.md`,
  `docs/review/03_REVISION_RESPONSE.md`.
- Targeted competitor verification: `docs/review/04_COMPETITOR_VERIFICATION.md`.
- Current approvals and unresolved decisions: `docs/05_TEAM_DECISIONS.md`.
- Proposed scientific tasks, dependencies and acceptance gates:
  `docs/06_SCIENTIFIC_DEVELOPMENT_PLAN.md`.
- Collaboration and handoff: `docs/07_COLLABORATION_GUIDE.md`.
- Data fields: `docs/01_DATASET_REVIEW.md`, `docs/04_COLUMN_INVENTORY.md`.
- Acquisition and data policy: `docs/02_DOWNLOAD_GUIDE.md`, `data/README.md`;
  provenance: `data/download_manifest.csv`.
- Setup and verification: `README.md`; entry points: `scripts/` and
  `literature/audit_design_coverage.py`.

## Authorization and scientific limits

Public downloads, descriptive audits and proposal refinement are authorized.
Research implementations, fitted models, generator calibration and simulations
require explicit approval of G1 and the execution plan. The operational plan
is a draft, not execution approval. All three investigators review scientific
decisions jointly. Partial approvals are not three-person agreement.

Preserve identifiers and missing values locally. Do not treat method differences
as known biological loss, cross-sectional age as longitudinal development, or
raw-anatomy ratings as surface-reconstruction QC. Define contrasts, populations,
support, scenario splits and seeds before inspecting effects. Keep 68 regions
in EB harmonization. Mark verified facts, inference and unknowns; never guarantee
novelty, calibration, power or publication. Do not invent results or approvals.

## Repository workflow

- Read only the context needed for the current task and its approval state.
- Propose and obtain approval before architecture or multi-file implementation;
  proceed directly for a small, clearly authorized correction.
- Use short-lived branches and Conventional Commits. Avoid concurrent edits to
  the same files. Subagents are optional for bounded work, never automatic.
- Do not push, merge or update `main`, `master` or `develop` without explicit
  approval. Review scientific changes jointly through pull requests.
- GitHub CLI `gh` is authorized for this repository. New account/service access,
  collaborator invitations and paid resources require user authorization.
- Never commit credentials, participant-level data, downloaded sources,
  notebook outputs or unreviewed execution artifacts. Keep exclusions in
  `.gitignore`; audit the tracked file list before publication.
- Run download modes sequentially: they share a manifest. Preserve the
  historical manifest; review changes instead of silently replacing provenance.
- Repository-only check: `python3 scripts/verify_repository.py`.
- Full local data check after reconstruction: `python3 scripts/verify_audit.py`.
- Do not add research dependencies until the execution plan is approved.
- Update the decision/task documents with completed work, remaining tasks,
  branch/PR/commit references, checks and blockers before handing off unfinished
  work. Keep status there, not in this context map.
