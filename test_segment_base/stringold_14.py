# Convert string to integer
def atoi(*args):
    """atoi(s [,base]) -> int
    Return the integer represented by the string s in the given
    base, which defaults to 10.  The string s must consist of one
    or more digits, possibly preceded by a sign.  If base is 0, it
    is chosen from the leading characters of s, 0 for octal, 0x or
    0X for hexadecimal.  If base is 16, a preceding 0x or 0X is
    accepted.
    """
    try:
        s = args[0]
    except IndexError:
        raise TypeError('function requires at least 1 argument: %d given' %
                        len(args))
    # Don't catch type error resulting from too many arguments to int().  The
    # error message isn't compatible but the error type is, and this function
    # is complicated enough already.
    if type(s) == _StringType:
        return _apply(_int, args)
    else:
        raise TypeError('argument 1: expected string, %s found' %
                        type(s).__name__)
