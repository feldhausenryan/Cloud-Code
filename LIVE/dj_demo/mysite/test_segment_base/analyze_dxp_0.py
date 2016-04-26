# If Python was built with -DDXPAIRS, sys.getdxp() returns a list of
# lists of ints.  Otherwise it returns just a list of ints.
def has_pairs(profile):
    """Returns True if the Python that produced the argument profile
    was built with -DDXPAIRS."""
    return len(profile) > 0 and isinstance(profile[0], list)
