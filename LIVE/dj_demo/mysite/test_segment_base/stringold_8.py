# Find substring, raise exception if not found
def index(s, *args):
    """index(s, sub [,start [,end]]) -> int
    Like find but raises ValueError when the substring is not found.
    """
    return _apply(s.index, args)
