# Find last substring, raise exception if not found
def rindex(s, *args):
    """rindex(s, sub [,start [,end]]) -> int
    Like rfind but raises ValueError when the substring is not found.
    """
    return s.rindex(*args)
