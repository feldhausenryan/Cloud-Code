#......................................
def put(a, indices, values, mode='raise'):
    """
    Set storage-indexed locations to corresponding values.
    This function is equivalent to `MaskedArray.put`, see that method
    for details.
    See Also
    --------
    MaskedArray.put
    """
    # We can't use 'frommethod', the order of arguments is different
    try:
        return a.put(indices, values, mode=mode)
    except AttributeError:
        return narray(a, copy=False).put(indices, values, mode=mode)
