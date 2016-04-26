# check_overflow is ignored
def fromlist(seq, type=None, shape=None, check_overflow=0, typecode=None, dtype=None):
    dtype = type2dtype(typecode, type, dtype, False)
    return np.array(seq, dtype)
