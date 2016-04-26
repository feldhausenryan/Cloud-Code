# -------------------------------------------------- source code extraction
def indentsize(line):
    """Return the indent size, in spaces, at the start of a line of text."""
    expline = string.expandtabs(line)
    return len(expline) - len(string.lstrip(expline))
