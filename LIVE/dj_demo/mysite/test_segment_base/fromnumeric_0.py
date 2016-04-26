# functions that are now methods
def _wrapit(obj, method, *args, **kwds):
    try:
        wrap = obj.__array_wrap__
    except AttributeError:
        wrap = None
    result = getattr(asarray(obj),method)(*args, **kwds)
    if wrap:
        if not isinstance(result, mu.ndarray):
            result = asarray(result)
        result = wrap(result)
    return result
