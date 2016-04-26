# ----------------------------------------------------------- type-checking
def ismodule(object):
    """Return true if the object is a module.
    Module objects provide these attributes:
        __doc__         documentation string
        __file__        filename (missing for built-in modules)"""
    return isinstance(object, types.ModuleType)
