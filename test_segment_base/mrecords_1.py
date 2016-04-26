#..............................................................................
def fromrecords(reclist, dtype=None, shape=None, formats=None, names=None,
                titles=None, aligned=False, byteorder=None,
                fill_value=None, mask=nomask):
    """Creates a MaskedRecords from a list of records.
    Parameters
    ----------
    reclist : sequence
        A list of records. Each element of the sequence is first converted
        to a masked array if needed. If a 2D array is passed as argument, it is
        processed line by line
    dtype : {None, dtype}, optional
        Data type descriptor.
    shape : {None,int}, optional
        Number of records. If None, ``shape`` is defined from the shape of the
        first array in the list.
    formats : {None, sequence}, optional
        Sequence of formats for each individual field. If None, the formats will
        be autodetected by inspecting the fields and selecting the highest dtype
        possible.
    names : {None, sequence}, optional
        Sequence of the names of each field.
    fill_value : {None, sequence}, optional
        Sequence of data to be used as filling values.
    mask : {nomask, sequence}, optional.
        External mask to apply on the data.
    Notes
    -----
    Lists of tuples should be preferred over lists of lists for faster processing.
    """
    # Grab the initial _fieldmask, if needed:
    _mask = getattr(reclist, '_mask', None)
    # Get the list of records.....
    try:
        nfields = len(reclist[0])
    except TypeError:
        nfields = len(reclist[0].dtype)
    if isinstance(reclist, ndarray):
        # Make sure we don't have some hidden mask
        if isinstance(reclist, MaskedArray):
            reclist = reclist.filled().view(ndarray)
        # Grab the initial dtype, just in case
        if dtype is None:
            dtype = reclist.dtype
        reclist = reclist.tolist()
    mrec = recfromrecords(reclist, dtype=dtype, shape=shape, formats=formats,
                          names=names, titles=titles,
                          aligned=aligned, byteorder=byteorder).view(mrecarray)
    # Set the fill_value if needed
    if fill_value is not None:
        mrec.fill_value = fill_value
    # Now, let's deal w/ the mask
    if mask is not nomask:
        mask = np.array(mask, copy=False)
        maskrecordlength = len(mask.dtype)
        if maskrecordlength:
            mrec._mask.flat = mask
        elif len(mask.shape) == 2:
            mrec._mask.flat = [tuple(m) for m in mask]
        else:
            mrec.__setmask__(mask)
    if _mask is not None:
        mrec._mask[:] = _mask
    return mrec
