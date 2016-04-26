# Note: copied from OInspect, kept here so the testing stuff doesn't create
# circular dependencies and is easier to reuse.
def getargspec(obj):
    """Get the names and default values of a function's arguments.
    A tuple of four things is returned: (args, varargs, varkw, defaults).
    'args' is a list of the argument names (it may contain nested lists).
    'varargs' and 'varkw' are the names of the * and ** arguments or None.
    'defaults' is an n-tuple of the default values of the last n arguments.
    Modified version of inspect.getargspec from the Python Standard
    Library."""
    if inspect.isfunction(obj):
        func_obj = obj
    elif inspect.ismethod(obj):
        func_obj = obj.im_func
    else:
        raise TypeError, 'arg is not a Python function'
    args, varargs, varkw = inspect.getargs(func_obj.func_code)
    return args, varargs, varkw, func_obj.func_defaults
