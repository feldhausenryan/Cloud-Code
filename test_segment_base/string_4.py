# Strip leading and trailing tabs and spaces
def strip(s, chars=None):
    """strip(s [,chars]) -> string
    Return a copy of the string s with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping.
    """
    return s.strip(chars)
