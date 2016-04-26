#==============================================================================
# Special method attributes
#==============================================================================
def get_meth_func(obj):
    """Return method function object"""
    if PY2:
        # Python 2
        return obj.im_func
    else:
        # Python 3
        return obj.__func__
