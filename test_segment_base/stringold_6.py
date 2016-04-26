# Split a string into a list of space/tab-separated words
def split(s, sep=None, maxsplit=0):
    """split(str [,sep [,maxsplit]]) -> list of strings
    Return a list of the words in the string s, using sep as the
    delimiter string.  If maxsplit is nonzero, splits into at most
    maxsplit words If sep is not specified, any whitespace string
    is a separator.  Maxsplit defaults to 0.
    (split and splitfields are synonymous)
    """
    return s.split(sep, maxsplit)
