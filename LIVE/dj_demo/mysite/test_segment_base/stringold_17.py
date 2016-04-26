# Right-justify a string
def rjust(s, width):
    """rjust(s, width) -> string
    Return a right-justified version of s, in a field of the
    specified width, padded with spaces as needed.  The string is
    never truncated.
    """
    n = width - len(s)
    if n <= 0: return s
    return ' '*n + s
