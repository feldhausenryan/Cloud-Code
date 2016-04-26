#XXX: I know, this function is now also implemented as is in utils/misc.py but
#     I'm kind of reluctant to import spyderlib in sitecustomize, even if this
#     import is very clean.
def monkeypatch_method(cls, patch_name):
    # This function's code was inspired from the following thread:
    # "[Python-Dev] Monkeypatching idioms -- elegant or ugly?"
    # by Robert Brewer <fumanchu at aminus.org>
    # (Tue Jan 15 19:13:25 CET 2008)
    """
    Add the decorated method to the given class; replace as needed.
    If the named method already exists on the given class, it will
    be replaced, and a reference to the old method is created as 
    cls._old<patch_name><name>. If the "_old_<patch_name>_<name>" attribute 
    already exists, KeyError is raised.
    """
    def decorator(func):
        fname = func.__name__
        old_func = getattr(cls, fname, None)
        if old_func is not None:
            # Add the old func to a list of old funcs.
            old_ref = "_old_%s_%s" % (patch_name, fname)
            #print old_ref, old_func
            old_attr = getattr(cls, old_ref, None)
            if old_attr is None:
                setattr(cls, old_ref, old_func)
            else:
                raise KeyError("%s.%s already exists."
                               % (cls.__name__, old_ref))
        setattr(cls, fname, func)
        return func
    return decorator
