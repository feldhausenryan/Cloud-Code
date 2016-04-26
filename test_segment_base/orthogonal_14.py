# Shifted Legendre              P^*_n(x)
def ps_roots(n, mu=0):
    """[x,w] = ps_roots(n)
    Returns the roots (x) of the nth order shifted Legendre polynomial, P^*_n(x),
    and weights (w) to use in Gaussian Quadrature over [0,1] with weighting
    function 1.
    """
    return js_roots(n,1.0,1.0,mu=mu)
