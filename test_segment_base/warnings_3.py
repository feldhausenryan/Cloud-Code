# Helper for _setoption()
def _getcategory(category):
    import re
    if not category:
        return Warning
    if re.match("^[a-zA-Z0-9_]+$", category):
        try:
            cat = eval(category)
        except NameError:
            raise _OptionError("unknown warning category: %r" % (category,))
    else:
        i = category.rfind(".")
        module = category[:i]
        klass = category[i+1:]
        try:
            m = __import__(module, None, None, [klass])
        except ImportError:
            raise _OptionError("invalid module name: %r" % (module,))
        try:
            cat = getattr(m, klass)
        except AttributeError:
            raise _OptionError("unknown warning category: %r" % (category,))
    if not issubclass(cat, Warning):
        raise _OptionError("invalid warning category: %r" % (category,))
    return cat
