# Find last substring, return -1 if not found
def rfind(s, *args):
    """rfind(s, sub [,start [,end]]) -> int
    Return the highest index in s where substring sub is found,
    such that sub is contained within s[start,end].  Optional
    arguments start and end are interpreted as in slice notation.
    Return -1 on failure.
    """
    return _apply(s.rfind, args)
