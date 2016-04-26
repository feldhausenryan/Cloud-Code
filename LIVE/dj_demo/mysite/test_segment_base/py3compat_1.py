#==============================================================================
# Function attributes
#==============================================================================
def get_func_code(func):
    """Return function code object"""
    if PY2:
        # Python 2
        return func.func_code
    else:
        # Python 3
        return func.__code__
