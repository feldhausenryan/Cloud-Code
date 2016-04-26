# Zero-fill a number, e.g., (12, 3) --> '012' and (-3, 3) --> '-03'
# Decadent feature: the argument may be a string or a number
# (Use of this is deprecated; it should be a string as with ljust c.s.)
def zfill(x, width):
    """zfill(x, width) -> string
    Pad a numeric string x with zeros on the left, to fill a field
    of the specified width.  The string x is never truncated.
    """
    if not isinstance(x, basestring):
        x = repr(x)
    return x.zfill(width)
