#................................................
def rank(obj):
    "maskedarray version of the numpy function."
    return np.rank(getdata(obj))
