# Ultraspherical (Gegenbauer)        C^(alpha)_n(x)
def cg_roots(n, alpha, mu=0):
    """[x,w] = cg_roots(n,alpha)
    Returns the roots (x) of the nth order Ultraspherical (Gegenbauer)
    polynomial, C^(alpha)_n(x), and weights (w) to use in Gaussian Quadrature
    over [-1,1] with weighting function (1-x**2)**(alpha-1/2) with alpha>-1/2.
    """
    return j_roots(n,alpha-0.5,alpha-0.5,mu=mu)
