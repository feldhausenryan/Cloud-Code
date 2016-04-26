# conds is a tuple of an array and a vector
#  giving the left-hand and the right-hand side
#  of the additional equations to add to B
def _find_user(xk, yk, order, conds, B):
    lh = conds[0]
    rh = conds[1]
    B = np.concatenate((B, lh), axis=0)
    w = np.concatenate((yk, rh), axis=0)
    M, N = B.shape
    if (M > N):
        raise ValueError("over-specification of conditions")
    elif (M < N):
        return _find_smoothest(xk, yk, order, None, B)
    else:
        return np.dual.solve(B, w)
