###############################################################################
# Graph laplacian
def laplacian(csgraph, normed=False, return_diag=False):
    """ Return the Laplacian matrix of a directed graph.
    For non-symmetric graphs the out-degree is used in the computation.
    Parameters
    ----------
    csgraph : array_like or sparse matrix, 2 dimensions
        compressed-sparse graph, with shape (N, N).
    normed : bool, optional
        If True, then compute normalized Laplacian.
    return_diag : bool, optional
        If True, then return diagonal as well as laplacian.
    Returns
    -------
    lap : ndarray
        The N x N laplacian matrix of graph.
    diag : ndarray
        The length-N diagonal of the laplacian matrix.
        diag is returned only if return_diag is True.
    Notes
    -----
    The Laplacian matrix of a graph is sometimes referred to as the
    "Kirchoff matrix" or the "admittance matrix", and is useful in many
    parts of spectral graph theory.  In particular, the eigen-decomposition
    of the laplacian matrix can give insight into many properties of the graph.
    For non-symmetric directed graphs, the laplacian is computed using the
    out-degree of each node.
    Examples
    --------
    >>> from scipy.sparse import csgraph
    >>> G = np.arange(5) * np.arange(5)[:, np.newaxis]
    >>> G
    array([[ 0,  0,  0,  0,  0],
           [ 0,  1,  2,  3,  4],
           [ 0,  2,  4,  6,  8],
           [ 0,  3,  6,  9, 12],
           [ 0,  4,  8, 12, 16]])
    >>> csgraph.laplacian(G, normed=False)
    array([[  0,   0,   0,   0,   0],
           [  0,   9,  -2,  -3,  -4],
           [  0,  -2,  16,  -6,  -8],
           [  0,  -3,  -6,  21, -12],
           [  0,  -4,  -8, -12,  24]])
    """
    if csgraph.ndim != 2 or csgraph.shape[0] != csgraph.shape[1]:
        raise ValueError('csgraph must be a square matrix or array')
    if normed and (np.issubdtype(csgraph.dtype, np.int)
                   or np.issubdtype(csgraph.dtype, np.uint)):
        csgraph = csgraph.astype(np.float)
    if isspmatrix(csgraph):
        return _laplacian_sparse(csgraph, normed=normed,
                                 return_diag=return_diag)
    else:
        return _laplacian_dense(csgraph, normed=normed,
                                return_diag=return_diag)
