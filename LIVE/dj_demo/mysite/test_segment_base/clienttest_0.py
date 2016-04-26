# test decorator for skipping tests when libraries are unavailable
def skip_without(*names):
    """skip a test if some names are not importable"""
    @decorator
    def skip_without_names(f, *args, **kwargs):
        """decorator to skip tests in the absence of numpy."""
        for name in names:
            try:
                __import__(name)
            except ImportError:
                raise SkipTest
        return f(*args, **kwargs)
    return skip_without_names
