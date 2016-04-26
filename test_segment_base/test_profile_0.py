#-----------------------------------------------------------------------------
# Test functions
#-----------------------------------------------------------------------------
def win32_without_pywin32():
    if sys.platform == 'win32':
        try:
            import pywin32
        except ImportError:
            return True
    return False
