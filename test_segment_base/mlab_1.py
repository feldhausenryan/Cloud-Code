##################################################
# Linear interpolation algorithms
##################################################
def less_simple_linear_interpolation( x, y, xi, extrap=False ):
    """
    This function provides simple (but somewhat less so than
    :func:`cbook.simple_linear_interpolation`) linear interpolation.
    :func:`simple_linear_interpolation` will give a list of point
    between a start and an end, while this does true linear
    interpolation at an arbitrary set of points.
    This is very inefficient linear interpolation meant to be used
    only for a small number of points in relatively non-intensive use
    cases.  For real linear interpolation, use scipy.
    """
    if cbook.is_scalar(xi): xi = [xi]
    x = np.asarray(x)
    y = np.asarray(y)
    xi = np.asarray(xi)
    s = list(y.shape)
    s[0] = len(xi)
    yi = np.tile( np.nan, s )
    for ii,xx in enumerate(xi):
        bb = x == xx
        if np.any(bb):
            jj, = np.nonzero(bb)
            yi[ii] = y[jj[0]]
        elif xx<x[0]:
            if extrap:
                yi[ii] = y[0]
        elif xx>x[-1]:
            if extrap:
                yi[ii] = y[-1]
        else:
            jj, = np.nonzero(x<xx)
            jj = max(jj)
            yi[ii] = y[jj] + (xx-x[jj])/(x[jj+1]-x[jj]) * (y[jj+1]-y[jj])
    return yi
