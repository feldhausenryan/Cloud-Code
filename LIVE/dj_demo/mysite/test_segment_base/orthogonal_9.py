# Chebyshev of the first kind        C_n(x)
def c_roots(n, mu=0):
    """[x,w] = c_roots(n)
    Returns the roots (x) of the nth order Chebyshev (of the first kind)
    polynomial, C_n(x), and weights (w) to use in Gaussian Quadrature
    over [-2,2] with weighting function (1-(x/2)**2)**(-1/2).
    """
    if mu:
        [x,w,mu0] = j_roots(n,-0.5,-0.5,mu=1)
        return [x*2,w,mu0]
    else:
        [x,w] = j_roots(n,-0.5,-0.5,mu=0)
        return [x*2,w]
