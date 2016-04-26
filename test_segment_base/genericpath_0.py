# Does a path exist?
# This is false for dangling symbolic links on systems that support them.
def exists(path):
    """Test whether a path exists.  Returns False for broken symbolic links"""
    try:
        os.stat(path)
    except os.error:
        return False
    return True
