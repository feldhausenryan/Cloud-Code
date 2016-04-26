# Convert string to float
def atof(s):
    """atof(s) -> float
    Return the floating point number represented by the string s.
    """
    if type(s) == _StringType:
        return _float(s)
    else:
        raise TypeError('argument 1: expected string, %s found' %
                        type(s).__name__)
