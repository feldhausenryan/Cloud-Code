# Chebyshev of the second kind
#    U_n(x) = (n+1)! sqrt(pi) / (2*_gam(n+3./2)) * P^(1/2,1/2)_n(x)
def u_roots(n, mu=0):
    """[x,w] = u_roots(n)
    Returns the roots (x) of the nth order Chebyshev (of the second kind)
    polynomial, U_n(x), and weights (w) to use in Gaussian Quadrature
    over [-1,1] with weighting function (1-x**2)**1/2.
    """
    return j_roots(n,0.5,0.5,mu=mu)
