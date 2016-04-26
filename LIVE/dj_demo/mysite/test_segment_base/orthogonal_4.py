# Hermite  1                         H_n(x)
def h_roots(n, mu=0):
    """[x,w] = h_roots(n)
    Returns the roots (x) of the nth order Hermite polynomial,
    H_n(x), and weights (w) to use in Gaussian Quadrature over
    [-inf,inf] with weighting function exp(-x**2).
    """
    if n < 1:
        raise ValueError("n must be positive.")
    sbn_H = lambda k: sqrt(k/2)  # from recurrence relation
    an_H = lambda k: 0*k
    mu0 = sqrt(pi)               # integral of weight over interval
    val = gen_roots_and_weights(n,an_H,sbn_H,mu0)
    if mu:
        return val + [mu0]
    else:
        return val
