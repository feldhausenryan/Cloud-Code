# Generalized Laguerre               L^(alpha)_n(x)
def la_roots(n, alpha, mu=0):
    """[x,w] = la_roots(n,alpha)
    Returns the roots (x) of the nth order generalized (associated) Laguerre
    polynomial, L^(alpha)_n(x), and weights (w) to use in Gaussian quadrature over
    [0,inf] with weighting function exp(-x) x**alpha with alpha > -1.
    """
    if not all(alpha > -1):
        raise ValueError("alpha > -1")
    if n < 1:
        raise ValueError("n must be positive.")
    (p,q) = (alpha,0.0)
    sbn_La = lambda k: -sqrt(k*(k + p))  # from recurrence relation
    an_La = lambda k: 2*k + p + 1
    mu0 = cephes.gamma(alpha+1)           # integral of weight over interval
    val = gen_roots_and_weights(n,an_La,sbn_La,mu0)
    if mu:
        return val + [mu0]
    else:
        return val
