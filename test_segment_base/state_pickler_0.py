######################################################################
# Internal Utility functions.
######################################################################
def _get_file_read(f):
    if hasattr(f, 'read'):
        return f
    elif isinstance(f, basestring):
        return open(f, 'rb')
    else:
        raise TypeError, 'Given object is neither a file or String'
