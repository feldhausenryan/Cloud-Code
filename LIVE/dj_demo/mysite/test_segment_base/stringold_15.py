# Convert string to long integer
def atol(*args):
    """atol(s [,base]) -> long
    Return the long integer represented by the string s in the
    given base, which defaults to 10.  The string s must consist
    of one or more digits, possibly preceded by a sign.  If base
    is 0, it is chosen from the leading characters of s, 0 for
    octal, 0x or 0X for hexadecimal.  If base is 16, a preceding
    0x or 0X is accepted.  A trailing L or l is not accepted,
    unless base is 0.
    """
    try:
        s = args[0]
    except IndexError:
        raise TypeError('function requires at least 1 argument: %d given' %
                        len(args))
    # Don't catch type error resulting from too many arguments to long().  The
    # error message isn't compatible but the error type is, and this function
    # is complicated enough already.
    if type(s) == _StringType:
        return _apply(_long, args)
    else:
        raise TypeError('argument 1: expected string, %s found' %
                        type(s).__name__)
