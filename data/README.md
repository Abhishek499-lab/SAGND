# SAGND Data Directory

## Stage 3 — Deep Dataset Discovery

Stage 3 searched the Google Drive for potential source files for the
2,960-cell integrated human pancreatic scRNA-seq dataset described in
the SAGND manuscript.

### Files generated

- `stage3_dataset_candidates.csv`
- `stage3_structural_inspection.csv`
- `stage3_discovery_summary.json`

### Current scan

- Total Drive files scanned: 10329
- Potential data files: 5667
- Files with `2960` in filename: 0
- Pancreatic/single-cell named candidates: 8
- Structural 2960 matches: 3

No biological SAGND processing is performed in this stage.


## Stage 5 — Reverse Source Tracing

This stage investigated the provenance of the 2,960-cell dataset described
in the SAGND manuscript.

The existing `pancreas.h5ad.h5` candidate was structurally validated and
source-related metadata/files were searched.

Reports:

- `stage5_filename_source_trace.csv`
- `stage5_content_source_trace.csv`
- `stage5_2960_row_candidates.csv`
- `stage5_known_human_pancreas_trace.csv`
- `stage5_source_trace_summary.json`

No SAGND biological processing was performed.
