#..............................................................................
def compress_rowcols(x, axis=None):
    """
    Suppress the rows and/or columns of a 2-D array that contain
    masked values.
    The suppression behavior is selected with the `axis` parameter.
    - If axis is None, both rows and columns are suppressed.
    - If axis is 0, only rows are suppressed.
    - If axis is 1 or -1, only columns are suppressed.
    Parameters
    ----------
    axis : int, optional
        Axis along which to perform the operation. Default is None.
    Returns
    -------
    compressed_array : ndarray
        The compressed array.
    Examples
    --------
    >>> x = np.ma.array(np.arange(9).reshape(3, 3), mask=[[1, 0, 0],
    ...                                                   [1, 0, 0],
    ...                                                   [0, 0, 0]])
    >>> x
    masked_array(data =
     [[-- 1 2]
     [-- 4 5]
     [6 7 8]],
                 mask =
     [[ True False False]
     [ True False False]
     [False False False]],
           fill_value = 999999)
    >>> np.ma.extras.compress_rowcols(x)
    array([[7, 8]])
    >>> np.ma.extras.compress_rowcols(x, 0)
    array([[6, 7, 8]])
    >>> np.ma.extras.compress_rowcols(x, 1)
    array([[1, 2],
           [4, 5],
           [7, 8]])
    """
    x = asarray(x)
    if x.ndim != 2:
        raise NotImplementedError("compress2d works for 2D arrays only.")
    m = getmask(x)
    # Nothing is masked: return x
    if m is nomask or not m.any():
        return x._data
    # All is masked: return empty
    if m.all():
        return nxarray([])
    # Builds a list of rows/columns indices
    (idxr, idxc) = (range(len(x)), range(x.shape[1]))
    masked = m.nonzero()
    if not axis:
        for i in np.unique(masked[0]):
            idxr.remove(i)
    if axis in [None, 1, -1]:
        for j in np.unique(masked[1]):
            idxc.remove(j)
    return x._data[idxr][:, idxc]
