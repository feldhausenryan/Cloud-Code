##
# 10.01.2006, c
def configure( **kwargs ):
    """
    Valid keyword arguments with defaults (other ignored):
      assumeSortedIndices = False
    Umfpack requires a CSR/CSC matrix to have sorted column/row indices. If
    sure that the matrix fulfills this, pass assumeSortedIndices =
    True to gain some speed.
    """
    if 'assumeSortedIndices' in kwargs:
        globals()['assumeSortedIndices'] = kwargs['assumeSortedIndices']
