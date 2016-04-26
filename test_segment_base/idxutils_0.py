# Utility functions
def infType(dtype, itemsize, sign=+1):
    """Return a superior limit for maximum representable data type"""
    assert sign in [-1, +1]
    if dtype.kind == "S":
        if sign < 0:
            return "\x00"*itemsize
        else:
            return "\xff"*itemsize
    try:
        return infinityMap[dtype.name][sign >= 0]
    except KeyError:
        raise TypeError("Type %s is not supported" % dtype.name)
