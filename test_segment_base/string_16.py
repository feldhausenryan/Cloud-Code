# Convert string to integer
def atoi(s , base=10):
    """atoi(s [,base]) -> int
    Return the integer represented by the string s in the given
    base, which defaults to 10.  The string s must consist of one
    or more digits, possibly preceded by a sign.  If base is 0, it
    is chosen from the leading characters of s, 0 for octal, 0x or
    0X for hexadecimal.  If base is 16, a preceding 0x or 0X is
    accepted.
    """
    return _int(s, base)
