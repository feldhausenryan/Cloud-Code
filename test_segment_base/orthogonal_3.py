# Laguerre                      L_n(x)
def l_roots(n, mu=0):
    """[x,w] = l_roots(n)
    Returns the roots (x) of the nth order Laguerre polynomial, L_n(x),
    and weights (w) to use in Gaussian Quadrature over [0,inf] with weighting
    function exp(-x).
    """
    return la_roots(n,0.0,mu=mu)
