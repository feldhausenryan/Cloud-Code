######################################################################
# Utility functions.
######################################################################
def is_filter(object):
    from mayavi.core.filter import Filter
    return isinstance(object, Filter)
