# Substring replacement (global)
def replace(s, old, new, maxsplit=0):
    """replace (str, old, new[, maxsplit]) -> string
    Return a copy of string str with all occurrences of substring
    old replaced by new. If the optional argument maxsplit is
    given, only the first maxsplit occurrences are replaced.
    """
    return s.replace(old, new, maxsplit)
