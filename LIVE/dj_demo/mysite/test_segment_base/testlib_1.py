# duplicate definition from unittest2 of the _deprecate decorator
def _deprecate(original_func):
    def deprecated_func(*args, **kwargs):
        warnings.warn(
            ('Please use %s instead.' % original_func.__name__),
            DeprecationWarning, 2)
        return original_func(*args, **kwargs)
    return deprecated_func
