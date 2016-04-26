# matrix inversion
def inv(a, overwrite_a=False, check_finite=True):
    """
    Compute the inverse of a matrix.
    Parameters
    ----------
    a : array_like
        Square matrix to be inverted.
    overwrite_a : bool, optional
        Discard data in `a` (may improve performance). Default is False.
    check_finite : boolean, optional
        Whether to check the input matrixes contain only finite numbers.
        Disabling may give a performance gain, but may result to problems
        (crashes, non-termination) if the inputs do contain infinities or NaNs.
    Returns
    -------
    ainv : ndarray
        Inverse of the matrix `a`.
    Raises
    ------
    LinAlgError :
        If `a` is singular.
    ValueError :
        If `a` is not square, or not 2-dimensional.
    Examples
    --------
    >>> a = np.array([[1., 2.], [3., 4.]])
    >>> sp.linalg.inv(a)
    array([[-2. ,  1. ],
           [ 1.5, -0.5]])
    >>> np.dot(a, sp.linalg.inv(a))
    array([[ 1.,  0.],
           [ 0.,  1.]])
    """
    if check_finite:
        a1 = np.asarray_chkfinite(a)
    else:
        a1 = np.asarray(a)
    if len(a1.shape) != 2 or a1.shape[0] != a1.shape[1]:
        raise ValueError('expected square matrix')
    overwrite_a = overwrite_a or _datacopied(a1, a)
    #XXX: I found no advantage or disadvantage of using finv.
