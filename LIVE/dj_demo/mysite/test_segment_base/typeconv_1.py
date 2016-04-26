#if both typecode and dtype are None
#  return None
def convtypecode2(typecode, dtype=None):
    if dtype is None:
        if typecode is None:
            return None
        else:
            try:
                return oldtype2dtype[typecode]
            except:
                return np.dtype(typecode)
    else:
        return dtype
