##################################################
# Vector and path length geometry calculations
##################################################
def vector_lengths( X, P=2., axis=None ):
    """
    Finds the length of a set of vectors in *n* dimensions.  This is
    like the :func:`numpy.norm` function for vectors, but has the ability to
    work over a particular axis of the supplied array or matrix.
    Computes ``(sum((x_i)^P))^(1/P)`` for each ``{x_i}`` being the
    elements of *X* along the given axis.  If *axis* is *None*,
    compute over all elements of *X*.
    """
    X = np.asarray(X)
    return (np.sum(X**(P),axis=axis))**(1./P)
