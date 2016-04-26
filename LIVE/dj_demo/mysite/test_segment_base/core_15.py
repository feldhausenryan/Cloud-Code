#####--------------------------------------------------------------------------
#---- --- Pickling ---
#####--------------------------------------------------------------------------
def dump(a, F):
    """
    Pickle a masked array to a file.
    This is a wrapper around ``cPickle.dump``.
    Parameters
    ----------
    a : MaskedArray
        The array to be pickled.
    F : str or file-like object
        The file to pickle `a` to. If a string, the full path to the file.
    """
    if not hasattr(F, 'readline'):
        F = open(F, 'w')
    return cPickle.dump(a, F)
