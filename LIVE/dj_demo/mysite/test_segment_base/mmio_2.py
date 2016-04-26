#-------------------------------------------------------------------------------
def mmwrite(target, a, comment='', field=None, precision=None):
    """
    Writes the sparse or dense matrix A to a Matrix Market formatted file.
    Parameters
    ----------
    target : file
        Matrix Market filename (extension .mtx) or open file object
    a : array like
        Sparse or full matrix
    comment : str, optional
        comments to be prepended to the Matrix Market file
    field : str, optional
        Either 'real', 'complex', 'pattern', or 'integer'.
    precision : int, optional
        Number of digits to display for real or complex values.
    """
    MMFile().write(target, a, comment, field, precision)
