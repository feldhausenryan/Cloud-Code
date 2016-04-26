#-------------------------------------------------------------------------------
def mmread(source):
    """
    Reads the contents of a Matrix Market file 'filename' into a matrix.
    Parameters
    ----------
    source : file
        Matrix Market filename (extensions .mtx, .mtz.gz)
        or open file object.
    Returns
    -------
    a:
        Sparse or full matrix
    """
    return MMFile().read(source)
