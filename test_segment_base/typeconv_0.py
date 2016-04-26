# converts typecode=None to int
def convtypecode(typecode, dtype=None):
    if dtype is None:
        try:
            return oldtype2dtype[typecode]
        except:
            return np.dtype(typecode)
    else:
        return dtype
