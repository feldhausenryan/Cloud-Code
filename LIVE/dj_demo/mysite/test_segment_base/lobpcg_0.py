##
# 21.05.2007, c
def as2d( ar ):
    """
    If the input array is 2D return it, if it is 1D, append a dimension,
    making it a column vector.
    """
    if ar.ndim == 2:
        return ar
    else: # Assume 1!
        aux = np.array( ar, copy = False )
        aux.shape = (ar.shape[0], 1)
        return aux
