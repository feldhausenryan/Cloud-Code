# backwards compatibility alias
def xfileref_role(*args, **kwds):
    warnings.warn('xfileref_role is deprecated, use XRefRole',
                  DeprecationWarning, stacklevel=2)
    return XRefRole()(*args, **kwds)
