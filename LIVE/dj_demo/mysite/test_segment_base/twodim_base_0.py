# borrowed from John Hunter and matplotlib
def vander(x, N=None):
    """
    Generate a Van der Monde matrix.
    The columns of the output matrix are decreasing powers of the input
    vector.  Specifically, the `i`-th output column is the input vector
    raised element-wise to the power of ``N - i - 1``.  Such a matrix with
    a geometric progression in each row is named for Alexandre-Theophile
    Vandermonde.
    Parameters
    ----------
    x : array_like
        1-D input array.
    N : int, optional
        Order of (number of columns in) the output.  If `N` is not specified,
        a square array is returned (``N = len(x)``).
    Returns
    -------
    out : ndarray
        Van der Monde matrix of order `N`.  The first column is ``x^(N-1)``,
        the second ``x^(N-2)`` and so forth.
    Examples
    --------
    >>> x = np.array([1, 2, 3, 5])
    >>> N = 3
    >>> np.vander(x, N)
    array([[ 1,  1,  1],
           [ 4,  2,  1],
           [ 9,  3,  1],
           [25,  5,  1]])
    >>> np.column_stack([x**(N-1-i) for i in range(N)])
    array([[ 1,  1,  1],
           [ 4,  2,  1],
           [ 9,  3,  1],
           [25,  5,  1]])
    >>> x = np.array([1, 2, 3, 5])
    >>> np.vander(x)
    array([[  1,   1,   1,   1],
           [  8,   4,   2,   1],
           [ 27,   9,   3,   1],
           [125,  25,   5,   1]])
    The determinant of a square Vandermonde matrix is the product
    of the differences between the values of the input vector:
    >>> np.linalg.det(np.vander(x))
    48.000000000000043
    >>> (5-3)*(5-2)*(5-1)*(3-2)*(3-1)*(2-1)
    48
    """
    x = asarray(x)
    if N is None:
        N=len(x)
    X = ones( (len(x),N), x.dtype)
    for i in range(N - 1):
        X[:,i] = x**(N - i - 1)
    return X
