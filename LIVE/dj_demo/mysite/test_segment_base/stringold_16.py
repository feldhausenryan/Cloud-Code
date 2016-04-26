# Left-justify a string
def ljust(s, width):
    """ljust(s, width) -> string
    Return a left-justified version of s, in a field of the
    specified width, padded with spaces as needed.  The string is
    never truncated.
    """
    n = width - len(s)
    if n <= 0: return s
    return s + ' '*n
