#TODO move this to a matrix gallery and add unittests
def poisson2d(N,dtype='d',format=None):
    """
    Return a sparse matrix for the 2D Poisson problem
    with standard 5-point finite difference stencil on a
    square N-by-N grid.
    """
    if N == 1:
        diags   = asarray( [[4]],dtype=dtype)
        return dia_matrix((diags,[0]), shape=(1,1)).asformat(format)
    offsets = array([0,-N,N,-1,1])
    diags = empty((5,N**2),dtype=dtype)
    diags[0]  =  4 #main diagonal
    diags[1:] = -1 #all offdiagonals
    diags[3,N-1::N] = 0  #first lower diagonal
    diags[4,N::N]   = 0  #first upper diagonal
    return dia_matrix((diags,offsets),shape=(N**2,N**2)).asformat(format)
