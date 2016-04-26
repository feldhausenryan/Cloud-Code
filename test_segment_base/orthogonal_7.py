# Chebyshev of the first kind: T_n(x)  = n! sqrt(pi) / _gam(n+1./2)* P^(-1/2,-1/2)_n(x)
#  Computed anew.
def t_roots(n, mu=0):
    """[x,w] = t_roots(n)
    Returns the roots (x) of the nth order Chebyshev (of the first kind)
    polynomial, T_n(x), and weights (w) to use in Gaussian Quadrature
    over [-1,1] with weighting function (1-x**2)**(-1/2).
    """
    if n < 1:
        raise ValueError("n must be positive.")
    # from recurrence relation
    sbn_J = lambda k: np.where(k==1,sqrt(2)/2.0,0.5)
    an_J = lambda k: 0.0*k
    g = cephes.gamma
    mu0 = pi
    val = gen_roots_and_weights(n,an_J,sbn_J,mu0)
    if mu:
        return val + [mu0]
    else:
        return val
