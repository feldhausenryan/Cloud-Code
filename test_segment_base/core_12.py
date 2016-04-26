#
def size(obj, axis=None):
    "maskedarray version of the numpy function."
    return np.size(getdata(obj), axis)
