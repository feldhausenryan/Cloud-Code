# Format the result message that the parser produces when running in debug mode.
def format_result(r):
    repr_str = repr(r)
    if '\n' in repr_str: repr_str = repr(repr_str)
    if len(repr_str) > resultlimit:
        repr_str = repr_str[:resultlimit]+" ..."
    result = "<%s @ 0x%x> (%s)" % (type(r).__name__,id(r),repr_str)
    return result
