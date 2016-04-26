#-------------------------------------------------------------------------------
def mminfo(source):
    """
    Queries the contents of the Matrix Market file 'filename' to
    extract size and storage information.
    Parameters
    ----------
    source : file
        Matrix Market filename (extension .mtx) or open file object
    Returns
    -------
    rows,cols : int
       Number of matrix rows and columns
    entries : int
        Number of non-zero entries of a sparse matrix
        or rows*cols for a dense matrix
    format : str
        Either 'coordinate' or 'array'.
    field : str
        Either 'real', 'complex', 'pattern', or 'integer'.
    symm : str
        Either 'general', 'symmetric', 'skew-symmetric', or 'hermitian'.
    """
    return MMFile.info(source)
