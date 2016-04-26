#####--------------------------------------------------------------------------
def getdata(a, subok=True):
    """
    Return the data of a masked array as an ndarray.
    Return the data of `a` (if any) as an ndarray if `a` is a ``MaskedArray``,
    else return `a` as a ndarray or subclass (depending on `subok`) if not.
    Parameters
    ----------
    a : array_like
        Input ``MaskedArray``, alternatively a ndarray or a subclass thereof.
    subok : bool
        Whether to force the output to be a `pure` ndarray (False) or to
        return a subclass of ndarray if appropriate (True, default).
    See Also
    --------
    getmask : Return the mask of a masked array, or nomask.
    getmaskarray : Return the mask of a masked array, or full array of False.
    Examples
    --------
    >>> import numpy.ma as ma
    >>> a = ma.masked_equal([[1,2],[3,4]], 2)
    >>> a
    masked_array(data =
     [[1 --]
     [3 4]],
          mask =
     [[False  True]
     [False False]],
          fill_value=999999)
    >>> ma.getdata(a)
    array([[1, 2],
           [3, 4]])
    Equivalently use the ``MaskedArray`` `data` attribute.
    >>> a.data
    array([[1, 2],
           [3, 4]])
    """
    try:
        data = a._data
    except AttributeError:
        data = np.array(a, copy=False, subok=subok)
    if not subok:
        return data.view(ndarray)
    return data
