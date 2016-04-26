# Jacobi Polynomials 1               P^(alpha,beta)_n(x)
def j_roots(n, alpha, beta, mu=0):
    """[x,w] = j_roots(n,alpha,beta)
    Returns the roots (x) of the nth order Jacobi polynomial, P^(alpha,beta)_n(x)
    and weights (w) to use in Gaussian Quadrature over [-1,1] with weighting
    function (1-x)**alpha (1+x)**beta with alpha,beta > -1.
    """
    if any(alpha <= -1) or any(beta <= -1):
        raise ValueError("alpha and beta must be greater than -1.")
    if n < 1:
        raise ValueError("n must be positive.")
    olderr = np.seterr(all='ignore')
    try:
        (p,q) = (alpha,beta)
        # from recurrence relations
        sbn_J = lambda k: 2.0/(2.0*k+p+q)*sqrt((k+p)*(k+q)/(2*k+q+p+1)) * \
                    (np.where(k==1,1.0,sqrt(k*(k+p+q)/(2.0*k+p+q-1))))
        if any(p == q):  # XXX any or all???
            an_J = lambda k: 0.0*k
        else:
            an_J = lambda k: np.where(k==0,(q-p)/(p+q+2.0),
                                   (q*q - p*p)/((2.0*k+p+q)*(2.0*k+p+q+2)))
        g = cephes.gamma
        mu0 = 2.0**(p+q+1)*g(p+1)*g(q+1)/(g(p+q+2))
        val = gen_roots_and_weights(n,an_J,sbn_J,mu0)
    finally:
        np.seterr(**olderr)
    if mu:
        return val + [mu0]
    else:
        return val
