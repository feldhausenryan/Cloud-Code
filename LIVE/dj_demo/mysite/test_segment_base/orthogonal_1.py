# Jacobi Polynomials shifted         G_n(p,q,x)
def js_roots(n, p1, q1, mu=0):
    """[x,w] = js_roots(n,p,q)
    Returns the roots (x) of the nth order shifted Jacobi polynomial, G_n(p,q,x),
    and weights (w) to use in Gaussian Quadrature over [0,1] with weighting
    function (1-x)**(p-q) x**(q-1) with p-q > -1 and q > 0.
    """
    # from recurrence relation
    if not ( any((p1 - q1) > -1) and any(q1 > 0) ):
        raise ValueError("(p - q) > -1 and q > 0 please.")
    if n <= 0:
        raise ValueError("n must be positive.")
    p,q = p1,q1
    sbn_Js = lambda k: sqrt(np.where(k==1,q*(p-q+1.0)/(p+2.0), \
                                  k*(k+q-1.0)*(k+p-1.0)*(k+p-q) \
                                  / ((2.0*k+p-2) * (2.0*k+p))))/(2*k+p-1.0)
    an_Js = lambda k: np.where(k==0,q/(p+1.0),(2.0*k*(k+p)+q*(p-1.0)) / ((2.0*k+p+1.0)*(2*k+p-1.0)))
    # could also use definition
    #  Gn(p,q,x) = constant_n * P^(p-q,q-1)_n(2x-1)
    #  so roots of Gn(p,q,x) are (roots of P^(p-q,q-1)_n + 1) / 2.0
    g = _gam
    # integral of weight over interval
    mu0 =  g(q)*g(p-q+1)/g(p+1)
    val = gen_roots_and_weights(n,an_Js,sbn_Js,mu0)
    if mu:
        return val + [mu0]
    else:
        return val
    # What code would look like using jacobi polynomial roots
    #if mu:
    #    [x,w,mut] = j_roots(n,p-q,q-1,mu=1)
    #    return [(x+1)/2.0,w,mu0]
    #else:
    #    [x,w] = j_roots(n,p-q,q-1,mu=0)
    #    return [(x+1)/2.0,w]
