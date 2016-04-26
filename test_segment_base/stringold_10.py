# Count non-overlapping occurrences of substring
def count(s, *args):
    """count(s, sub[, start[,end]]) -> int
    Return the number of occurrences of substring sub in string
    s[start:end].  Optional arguments start and end are
    interpreted as in slice notation.
    """
    return _apply(s.count, args)
