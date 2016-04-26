######################################################################
# Utility functions.
######################################################################
def get_version(obj):
    """Walks the class hierarchy and obtains the versions of the
    various classes and returns a list of tuples of the form
    ((class_name, module), version) in reverse order of the MRO.
    """
    res = []
    for cls in inspect.getmro(obj.__class__):
        class_name, module = cls.__name__, cls.__module__
        if module in ['__builtin__']:
            # No point in versioning builtins.
            continue
        try:
            version = cls.__version__
        except AttributeError:
            version = -1
        res.append( ( (class_name, module), version) )
    res.reverse()
    return res
