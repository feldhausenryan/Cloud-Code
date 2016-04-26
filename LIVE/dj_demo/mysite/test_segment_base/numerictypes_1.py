# Keep incrementing until a common type both can be coerced to
#  is found.  Otherwise, return None
def _find_common_coerce(a, b):
    if a > b:
        return a
    try:
        thisind = __test_types.index(a.char)
    except ValueError:
        return None
    return _can_coerce_all([a,b], start=thisind)
