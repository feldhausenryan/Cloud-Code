# Shifted Chebyshev of the first kind     T^*_n(x)
def ts_roots(n, mu=0):
    """[x,w] = ts_roots(n)
    Returns the roots (x) of the nth order shifted Chebyshev (of the first kind)
    polynomial, T^*_n(x), and weights (w) to use in Gaussian Quadrature
    over [0,1] with weighting function (x-x**2)**(-1/2).
    """
    return js_roots(n,0.0,0.5,mu=mu)
