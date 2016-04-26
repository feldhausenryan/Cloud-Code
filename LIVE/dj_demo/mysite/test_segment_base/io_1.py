#==============================================================================
# Text files Private I/O functions
#==============================================================================
def _imread_txt(filename):
    """Open text file image and return a NumPy array"""
    for delimiter in ('\t', ',', ' ', ';'):
        try:
            return np.loadtxt(filename, delimiter=delimiter)
        except ValueError:
            continue
    else:
        raise
