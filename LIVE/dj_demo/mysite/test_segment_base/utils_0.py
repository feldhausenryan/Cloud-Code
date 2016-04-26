# These functions are in the standalone mimelib version only because they've
# subsequently been fixed in the latest Python versions.  We use this to worm
# around broken older Pythons.
def parsedate(data):
    if not data:
        return None
    return _parsedate(data)
