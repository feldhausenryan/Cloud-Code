# Expand tabs in a string.
# Doesn't take non-printing chars into account, but does understand \n.
def expandtabs(s, tabsize=8):
    """expandtabs(s [,tabsize]) -> string
    Return a copy of the string s with all tab characters replaced
    by the appropriate number of spaces, depending on the current
    column, and the tabsize (default 8).
    """
    res = line = ''
    for c in s:
        if c == '\t':
            c = ' '*(tabsize - len(line) % tabsize)
        line = line + c
        if c == '\n':
            res = res + line
            line = ''
    return res + line
