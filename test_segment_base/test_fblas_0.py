# Since numpy.dot likely uses the same blas, use this routine
# to check.
def matrixmultiply(a, b):
    if len(b.shape) == 1:
        b_is_vector = True
        b = b[:,newaxis]
    else:
        b_is_vector = False
    assert_equal(a.shape[1], b.shape[0])
    c = zeros((a.shape[0], b.shape[1]), common_type(a, b))
    for i in xrange(a.shape[0]):
        for j in xrange(b.shape[1]):
            s = 0
            for k in xrange(a.shape[1]):
                s += a[i,k] * b[k, j]
            c[i,j] = s
    if b_is_vector:
        c = c.reshape((a.shape[0],))
    return c
