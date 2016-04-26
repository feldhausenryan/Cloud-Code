# Left-justify a string
def ljust(s, width, *args):
    """ljust(s, width[, fillchar]) -> string
    Return a left-justified version of s, in a field of the
    specified width, padded with spaces as needed.  The string is
    never truncated.  If specified the fillchar is used instead of spaces.
    """
    return s.ljust(width, *args)
