# Shifted Chebyshev of the second kind    U^*_n(x)
def us_roots(n, mu=0):
    """[x,w] = us_roots(n)
    Returns the roots (x) of the nth order shifted Chebyshev (of the second kind)
    polynomial, U^*_n(x), and weights (w) to use in Gaussian Quadrature
    over [0,1] with weighting function (x-x**2)**1/2.
    """
    return js_roots(n,2.0,1.5,mu=mu)
