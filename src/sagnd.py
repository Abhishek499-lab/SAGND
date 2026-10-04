import numpy as np
from sklearn.neighbors import NearestNeighbors


def build_knn_graph(X_pca, k=15):

    X_pca = np.asarray(X_pca, dtype=float)

    if X_pca.ndim != 2:
        raise ValueError(
            "X_pca must be a 2-dimensional matrix."
        )

    n_cells = X_pca.shape[0]

    if n_cells <= k:
        raise ValueError(
            "k must be smaller than the number of cells."
        )

    model = NearestNeighbors(
        n_neighbors=k + 1,
        metric="euclidean"
    )

    model.fit(X_pca)

    distances, indices = model.kneighbors(X_pca)

    neighbors = indices[:, 1:]
    distances = distances[:, 1:]

    return neighbors, distances


def compute_neighborhood_expression(X, neighbors):

    X = np.asarray(X, dtype=float)

    n_cells, n_genes = X.shape

    neighborhood = np.empty(
        (n_cells, n_genes),
        dtype=float
    )

    for i in range(n_cells):

        neighborhood[i] = np.mean(
            X[neighbors[i]],
            axis=0
        )

    return neighborhood


def compute_gene_specificity(X):

    X = np.asarray(X, dtype=float)

    n_cells = X.shape[0]

    if n_cells < 2:
        raise ValueError(
            "At least two cells are required."
        )

    gene_totals = X.sum(axis=0)

    gene_totals = np.where(
        gene_totals <= 0,
        1e-12,
        gene_totals
    )

    probabilities = X / gene_totals

    entropy = -np.sum(
        probabilities *
        np.log(probabilities + 1e-12),
        axis=0
    )

    maximum_entropy = np.log(n_cells)

    normalized_entropy = (
        entropy /
        maximum_entropy
    )

    specificity = (
        1.0 -
        normalized_entropy
    )

    return np.clip(
        specificity,
        0.0,
        1.0
    )


def sagnd(
    X,
    X_pca,
    k=15,
    alpha=0.5
):

    X = np.asarray(X, dtype=float)
    X_pca = np.asarray(X_pca, dtype=float)

    if X.shape[0] != X_pca.shape[0]:
        raise ValueError(
            "X and X_pca must contain the same number of cells."
        )

    neighbors, distances = build_knn_graph(
        X_pca,
        k=k
    )

    neighborhood = compute_neighborhood_expression(
        X,
        neighbors
    )

    specificity = compute_gene_specificity(
        X
    )

    weights = alpha * (
        1.0 -
        specificity
    )

    X_denoised = (
        X +
        neighborhood * weights
    ) / (
        1.0 +
        weights
    )

    return (
        X_denoised,
        specificity,
        neighbors,
        distances
    )
