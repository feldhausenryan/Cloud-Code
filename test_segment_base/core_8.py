#......................................
def left_shift (a, n):
    """
    Shift the bits of an integer to the left.
    This is the masked array version of `numpy.left_shift`, for details
    see that function.
    See Also
    --------
    numpy.left_shift
    """
    m = getmask(a)
    if m is nomask:
        d = umath.left_shift(filled(a), n)
        return masked_array(d)
    else:
        d = umath.left_shift(filled(a, 0), n)
        return masked_array(d, mask=m)
