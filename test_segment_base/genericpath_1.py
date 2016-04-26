# This follows symbolic links, so both islink() and isdir() can be true
# for the same path ono systems that support symlinks
def isfile(path):
    """Test whether a path is a regular file"""
    try:
        st = os.stat(path)
    except os.error:
        return False
    return stat.S_ISREG(st.st_mode)
