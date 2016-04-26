# Split a path in a drive specification (a drive letter followed by a
# colon) and the path specification.
# It is always true that drivespec + pathspec == p
def splitdrive(p):
    """Split a pathname into drive and path specifiers. Returns a 2-tuple
