# Character translation through look-up table.
def translate(s, table, deletions=""):
    """translate(s,table [,deletechars]) -> string
    Return a copy of the string s, where all characters occurring
    in the optional argument deletechars are removed, and the
    remaining characters have been mapped through the given
    translation table, which must be a string of length 256.
    """
    return s.translate(table, deletions)
