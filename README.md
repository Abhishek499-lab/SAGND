# SAGND

## Specificity-Aware Graph Neighborhood Denoising

SAGND is a graph-based computational framework for reducing
single-cell RNA-sequencing noise while limiting the smoothing of
genes with high transcriptional specificity.

The central principle is simple:

- highly specific genes receive less neighbourhood propagation
- broadly expressed genes receive greater neighbourhood refinement

## Workflow

1. Expression preprocessing
2. Highly variable gene selection
3. PCA-based representation
4. K-nearest-neighbour graph construction
5. Neighbourhood expression estimation
6. Gene-specific specificity estimation
7. Specificity-aware adaptive smoothing
8. Denoised expression matrix generation
9. Biological and structural validation

## Independent validation dataset

The independent reconstruction used for the final benchmark
contained:

- 3,695 cells
- 16,324 genes
- K = 10 nearest neighbours
- SAGND smoothing parameter alpha = 0.5

The historical manuscript workflow recorded a 2,960-cell ×
2,000-gene analysis state. The exact cell-level identity of that
historical subset could not be independently reconstructed from
the preserved notebook metadata, so the final independent
validation did not force a 2,960-cell reconstruction.

## Final benchmark

For the independent 3,695 × 16,324 input:

- mean absolute expression change: 0.0663431109760232
- median absolute expression change: 0.0143528908442872
- cell-level Spearman preservation: 0.972092
- gene-level Spearman preservation: 0.998908
- specificity–change Spearman correlation: -0.8456575101688742
- marker Spearman preservation: 0.758984
- marker Pearson preservation: 0.974058
- marker top-10% Jaccard: 0.803868
- cluster count in benchmark: 14.0
- silhouette score: 0.4330868316758863
- mean KNN Jaccard versus raw: 0.4942331096881849

## Specificity-aware behaviour

The final validation showed a strong inverse relationship between
gene specificity and the magnitude of the stored historical
SAGND change metric:

- Spearman rho = -0.8456575101688742
- low-specificity mean change = 0.206724
- high-specificity mean change = 0.000342

The corresponding permutation analysis used 5,000 permutations
with a fixed seed and provides an empirical null assessment of
the specificity–change association.

## Marker preservation

The seven evaluated pancreatic marker genes were:

INS, IAPP, MAFA, SST, PPY, PRSS1 and KRT19.

Across these markers:
- mean Spearman preservation = 0.972092
- mean Pearson preservation = 0.974058
- mean absolute change = None
- mean top-10% cell Jaccard = 0.803868

## Benchmark methods

The final same-input benchmark contains:

- SAGND
- KNN smoothing
- GraphSmooth-style simplified propagation
- MAGIC

MAGIC was **not executed** because of an environment/package
compatibility problem in the validation environment. Its numerical
benchmark fields are therefore intentionally left unavailable and
were not replaced with substituted values.

The GraphSmooth-style comparator is a simplified propagation
baseline and should not be interpreted as an exact historical
implementation of GraphSmooth.

## Reproducibility

The repository contains the final benchmark tables, marker-level
validation outputs, clustering/structure summaries, permutation-null
results, figures and audit records used for the reported validation.

Large biological matrices and raw datasets are intentionally not
stored in the Git repository. Their frozen local provenance and
integrity were verified separately.

## Repository status

Current GitHub branch: `main`

The local repository and GitHub `main` branch are synchronized.

The repository currently contains the approved publication and
validation outputs without committing the large raw biological
matrices.

## Important limitation

The independent validation input is 3,695 × 16,324. The preserved
historical notebook contains a 2,960 × 2,000 analysis state, but
the exact identity of those 2,960 cells could not be independently
reconstructed from the available notebook metadata.

Therefore, no artificial 2,960-cell selection was introduced into
the independent validation.

## Citation

Please cite the repository using the accompanying `CITATION.cff`
file.

## License

See the repository license and metadata files for the current
distribution terms.
