# not deprecated --- copy if necessary, view otherwise
def reshape(a, newshape, order='C'):
    """
    Gives a new shape to an array without changing its data.
    Parameters
    ----------
    a : array_like
        Array to be reshaped.
    newshape : int or tuple of ints
        The new shape should be compatible with the original shape. If
        an integer, then the result will be a 1-D array of that length.
        One shape dimension can be -1. In this case, the value is inferred
        from the length of the array and remaining dimensions.
    order : {'C', 'F', 'A'}, optional
        Determines whether the array data should be viewed as in C
        (row-major) order, FORTRAN (column-major) order, or the C/FORTRAN
        order should be preserved.
    Returns
    -------
    reshaped_array : ndarray
        This will be a new view object if possible; otherwise, it will
        be a copy.
    See Also
    --------
    ndarray.reshape : Equivalent method.
    Notes
    -----
    It is not always possible to change the shape of an array without
    copying the data. If you want an error to be raise if the data is copied,
    you should assign the new shape to the shape attribute of the array::
     >>> a = np.zeros((10, 2))
     # A transpose make the array non-contiguous
     >>> b = a.T
     # Taking a view makes it possible to modify the shape without modiying the
     # initial object.
     >>> c = b.view()
     >>> c.shape = (20)
     AttributeError: incompatible shape for a non-contiguous array
    Examples
    --------
    >>> a = np.array([[1,2,3], [4,5,6]])
    >>> np.reshape(a, 6)
    array([1, 2, 3, 4, 5, 6])
    >>> np.reshape(a, 6, order='F')
    array([1, 4, 2, 5, 3, 6])
    >>> np.reshape(a, (3,-1))       # the unspecified value is inferred to be 2
    array([[1, 2],
           [3, 4],
           [5, 6]])
    """
    try:
        reshape = a.reshape
    except AttributeError:
        return _wrapit(a, 'reshape', newshape, order=order)
    return reshape(newshape, order=order)
