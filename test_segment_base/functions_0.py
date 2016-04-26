#  If dtype is not None, then it is used
#  If type is not None, then it is used
#  If typecode is not None then it is used
#  If use_default is True, then the default
#   data-type is returned if all are None
def type2dtype(typecode, type, dtype, use_default=True):
    if dtype is None:
        if type is None:
            if use_default or typecode is not None:
                dtype = np.dtype(typecode)
        else:
            dtype = np.dtype(type)
    if use_default and dtype is None:
        dtype = np.dtype('int')
    return dtype
