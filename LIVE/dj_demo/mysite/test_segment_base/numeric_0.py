# Note: if x is a scalar and y = asarray(x), amin(y) FAILS but min(y) works
# Note: BUT IF z=convert(y,frac,frac), THEN min(z) FAILS!!!
def safe_min(a):
    # Return the minimum of the input array or the input if it is a scalar
    b = discard_nans(a)
    try:
        safemin = numpy.amin(b)
    except:
        safemin = b
    return safemin
