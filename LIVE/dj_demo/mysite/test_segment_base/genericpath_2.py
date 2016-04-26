# Is a path a directory?
# This follows symbolic links, so both islink() and isdir()
# can be true for the same path on systems that support symlinks
def isdir(s):
    """Return true if the pathname refers to an existing directory."""
    try:
        st = os.stat(s)
    except os.error:
        return False
    return stat.S_ISDIR(st.st_mode)
