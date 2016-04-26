# Find substring, return -1 if not found
def find(s, *args):
    """find(s, sub [,start [,end]]) -> in
    Return the lowest index in s where substring sub is found,
    such that sub is contained within s[start,end].  Optional
    arguments start and end are interpreted as in slice notation.
    Return -1 on failure.
    """
    return _apply(s.find, args)
