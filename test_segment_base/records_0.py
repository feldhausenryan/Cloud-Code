# shape must be 1-d if you use list of lists...
def fromrecords(recList, dtype=None, shape=None, formats=None, names=None,
                titles=None, aligned=False, byteorder=None):
    """ create a recarray from a list of records in text form
        The data in the same field can be heterogeneous, they will be promoted
        to the highest data type.  This method is intended for creating
        smaller record arrays.  If used to create large array without formats
        defined
        r=fromrecords([(2,3.,'abc')]*100000)
        it can be slow.
        If formats is None, then this will auto-detect formats. Use list of
        tuples rather than list of lists for faster processing.
    >>> r=np.core.records.fromrecords([(456,'dbe',1.2),(2,'de',1.3)],
    ... names='col1,col2,col3')
    >>> print r[0]
    (456, 'dbe', 1.2)
    >>> r.col1
    array([456,   2])
    >>> r.col2
    chararray(['dbe', 'de'],
          dtype='|S3')
    >>> import cPickle
    >>> print cPickle.loads(cPickle.dumps(r))
    [(456, 'dbe', 1.2) (2, 'de', 1.3)]
    """
    nfields = len(recList[0])
    if formats is None and dtype is None:  # slower
        obj = sb.array(recList, dtype=object)
        arrlist = [sb.array(obj[..., i].tolist()) for i in xrange(nfields)]
        return fromarrays(arrlist, formats=formats, shape=shape, names=names,
                          titles=titles, aligned=aligned, byteorder=byteorder)
    if dtype is not None:
        descr = sb.dtype((record, dtype))
    else:
        descr = format_parser(formats, names, titles, aligned, byteorder)._descr
    try:
        retval = sb.array(recList, dtype=descr)
    except TypeError:  # list of lists instead of list of tuples
        if (shape is None or shape == 0):
            shape = len(recList)
        if isinstance(shape, (int, long)):
            shape = (shape,)
        if len(shape) > 1:
            raise ValueError("Can only deal with 1-d array.")
        _array = recarray(shape, descr)
        for k in xrange(_array.size):
            _array[k] = tuple(recList[k])
        return _array
    else:
        if shape is not None and retval.shape != shape:
            retval.shape = shape
    res = retval.view(recarray)
    return res
