#--------------------
# Parsing actual data
#--------------------
def safe_float(x):
    """given a string x, convert it to a float. If the stripped string is a ?,
    return a Nan (missing value).
    Parameters
    ----------
    x : str
       string to convert
    Returns
    -------
    f : float
       where float can be nan
    Examples
    --------
    >>> safe_float('1')
    1.0
    >>> safe_float('1\\n')
    1.0
    >>> safe_float('?\\n')
    nan
    """
    if '?' in x:
        return np.nan
    else:
        return np.float(x)
