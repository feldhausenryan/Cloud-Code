# Hermite  2                         He_n(x)
def he_roots(n, mu=0):
    """[x,w] = he_roots(n)
    Returns the roots (x) of the nth order Hermite polynomial,
    He_n(x), and weights (w) to use in Gaussian Quadrature over
    [-inf,inf] with weighting function exp(-(x/2)**2).
    """
    if n < 1:
        raise ValueError("n must be positive.")
    sbn_He = lambda k: sqrt(k)   # from recurrence relation
    an_He  = lambda k: 0*k
    mu0 = sqrt(2*pi)             # integral of weight over interval
    val = gen_roots_and_weights(n,an_He,sbn_He,mu0)
    if mu:
        return val + [mu0]
    else:
        return val
