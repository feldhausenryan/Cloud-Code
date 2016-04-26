# Silence Py3k and other deprecation warnings
def ignore_deprecation_warnings(func):
    """Ignore the known DeprecationWarnings."""
    def wrapper(*args, **kw):
        with check_warnings(*_deprecations, quiet=True):
            return func(*args, **kw)
    return wrapper
