#####--------------------------------------------------------------------------
def filled(a, fill_value=None):
    """
    Return input as an array with masked data replaced by a fill value.
    If `a` is not a `MaskedArray`, `a` itself is returned.
    If `a` is a `MaskedArray` and `fill_value` is None, `fill_value` is set to
    ``a.fill_value``.
    Parameters
    ----------
    a : MaskedArray or array_like
        An input object.
    fill_value : scalar, optional
        Filling value. Default is None.
    Returns
    -------
    a : ndarray
        The filled array.
    See Also
    --------
    compressed
    Examples
    --------
    >>> x = np.ma.array(np.arange(9).reshape(3, 3), mask=[[1, 0, 0],
    ...                                                   [1, 0, 0],
    ...                                                   [0, 0, 0]])
    >>> x.filled()
    array([[999999,      1,      2],
           [999999,      4,      5],
           [     6,      7,      8]])
    """
    if hasattr(a, 'filled'):
        return a.filled(fill_value)
    elif isinstance(a, ndarray):
        # Should we check for contiguity ? and a.flags['CONTIGUOUS']:
        return a
    elif isinstance(a, dict):
        return np.array(a, 'O')
    else:
        return np.array(a)
