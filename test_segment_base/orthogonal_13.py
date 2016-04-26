# Legendre
def p_roots(n, mu=0):
    """[x,w] = p_roots(n)
    Returns the roots (x) of the nth order Legendre polynomial, P_n(x),
    and weights (w) to use in Gaussian Quadrature over [-1,1] with weighting
    function 1.
    """
    return j_roots(n,0.0,0.0,mu=mu)
