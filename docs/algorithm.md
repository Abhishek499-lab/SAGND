# SAGND Algorithm

## Specificity-Aware Graph Neighborhood Denoising

The initial implementation contains the following computational
components:

1. PCA-based cell representation
2. K-nearest-neighbour graph construction
3. Neighbourhood expression estimation
4. Gene-specific specificity estimation
5. Adaptive smoothing
6. Denoised expression generation

The biological motivation is to reduce stochastic technical variation
while protecting genes that show strong cell-type-specific expression.

The exact mathematical formulation will be finalized after complete
verification of the original study equations.
