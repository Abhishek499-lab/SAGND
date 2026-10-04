# SAGND

## Specificity-Aware Graph Neighborhood Denoising

SAGND is a graph-based computational framework designed to reduce
technical variation in single-cell RNA-sequencing data while
preserving biologically informative transcriptional patterns.

### Core concept

The framework uses cellular neighbourhood relationships together
with gene-specific transcriptional specificity.

The intended principle is:

- highly specific genes → less neighbourhood smoothing
- broadly expressed genes → greater neighbourhood refinement

### Workflow

1. Expression normalization
2. Highly variable gene selection
3. PCA
4. K-nearest-neighbour graph construction
5. Neighbourhood expression estimation
6. Gene-specific specificity estimation
7. Adaptive smoothing
8. Denoised expression matrix
9. Biological validation

### Planned validation

- UMAP
- Leiden clustering
- Silhouette analysis
- Marker-gene recovery
- Cell purity
- Graph connectivity
- PAGA
- Diffusion pseudotime
- Correlation preservation
- Comparative benchmarking

### Repository structure

SAGND/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   └── sagnd.py
├── scripts/
├── notebooks/
├── results/
│   ├── figures/
│   ├── tables/
│   └── metrics/
├── docs/
├── manuscript/
├── requirements.txt
├── CITATION.cff
├── VERSION.json
├── .gitignore
└── README.md

### Current status

Version: 0.1.0-dev

This is the initial computational development version.

The current specificity estimator is an initial implementation based
on the conceptual description available in the manuscript. The final
mathematical formulation will be verified before the repository is
used for final publication claims.

### Reproducibility

Computational analysis is being developed using Python and standard
scientific-computing libraries.

A fixed random seed is used where applicable.

Raw biological datasets will not be committed to the repository.
Dataset accession information and download instructions will be
provided separately.

### Citation

Citation information is provided in CITATION.cff.

### License

A final open-source license will be selected before public release.
