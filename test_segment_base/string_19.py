# Right-justify a string
def rjust(s, width, *args):
    """rjust(s, width[, fillchar]) -> string
    Return a right-justified version of s, in a field of the
    specified width, padded with spaces as needed.  The string is
    never truncated.  If specified the fillchar is used instead of spaces.
    """
    return s.rjust(width, *args)
