#
def shape(obj):
    "maskedarray version of the numpy function."
    return np.shape(getdata(obj))
