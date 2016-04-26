# Format stack entries when the parser is running in debug mode
def format_stack_entry(r):
    repr_str = repr(r)
    if '\n' in repr_str: repr_str = repr(repr_str)
    if len(repr_str) < 16:
        return repr_str
    else:
        return "<%s @ 0x%x>" % (type(r).__name__,id(r))
