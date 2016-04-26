# Split a string into a list of space/tab-separated words
def rsplit(s, sep=None, maxsplit=-1):
    """rsplit(s [,sep [,maxsplit]]) -> list of strings
    Return a list of the words in the string s, using sep as the
    delimiter string, starting at the end of the string and working
    to the front.  If maxsplit is given, at most maxsplit splits are
    done. If sep is not specified or is None, any whitespace string
    is a separator.
    """
    return s.rsplit(sep, maxsplit)
