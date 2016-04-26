######################################################################
# Utility functions.
######################################################################
def get_array_type(arr):
    """Returns if the array is a scalar ('scalars'), vector
    ('vectors') or tensor ('tensors').  It looks at the number of
    components to decide.  If it has a wierd number of components it
    returns the empty string.
    """
    n = arr.number_of_components
    ret = {1: 'scalars', 3: 'vectors', 4: 'scalars', 9:'tensors'}
    return ret.get(n) or ''
