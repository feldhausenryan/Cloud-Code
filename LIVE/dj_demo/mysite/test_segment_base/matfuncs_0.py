# implementation of Pade approximations of various degree using the algorithm presented in [Higham 2005]
# These should apply to both dense and sparse matricies.
# ident is the identity matrix, which matches A in being sparse or dense.
def _pade3(A, ident):
    b = (120., 60., 12., 1.)
    A2 = A.dot(A)
    U = A.dot(b[3]*A2 + b[1]*ident)
    V = b[2]*A2 + b[0]*ident
    return U,V
