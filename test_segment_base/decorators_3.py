#-----------------------------------------------------------------------------
# Utility functions for decorators
def module_not_available(module):
    """Can module be imported?  Returns true if module does NOT import.
    This is used to make a decorator to skip tests that require module to be
    available, but delay the 'import numpy' to test execution time.
    """
    try:
        mod = __import__(module)
        mod_not_avail = False
    except ImportError:
        mod_not_avail = True
    return mod_not_avail
