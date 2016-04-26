#..............................................................................
def power(a, b, third=None):
    """
    Returns element-wise base array raised to power from second array.
    This is the masked array version of `numpy.power`. For details see
    `numpy.power`.
    See Also
    --------
    numpy.power
    Notes
    -----
    The *out* argument to `numpy.power` is not supported, `third` has to be
    None.
    """
    if third is not None:
        raise MaskError("3-argument power not supported.")
    # Get the masks
    ma = getmask(a)
    mb = getmask(b)
    m = mask_or(ma, mb)
    # Get the rawdata
    fa = getdata(a)
    fb = getdata(b)
    # Get the type of the result (so that we preserve subclasses)
    if isinstance(a, MaskedArray):
        basetype = type(a)
    else:
        basetype = MaskedArray
    # Get the result and view it as a (subclass of) MaskedArray
    err_status = np.geterr()
    try:
        np.seterr(divide='ignore', invalid='ignore')
        result = np.where(m, fa, umath.power(fa, fb)).view(basetype)
    finally:
        np.seterr(**err_status)
    result._update_from(a)
    # Find where we're in trouble w/ NaNs and Infs
    invalid = np.logical_not(np.isfinite(result.view(ndarray)))
    # Add the initial mask
    if m is not nomask:
        if not (result.ndim):
            return masked
        result._mask = np.logical_or(m, invalid)
    # Fix the invalid parts
    if invalid.any():
        if not result.ndim:
            return masked
        elif result._mask is nomask:
            result._mask = invalid
        result._data[invalid] = result.fill_value
    return result
