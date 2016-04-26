######################################################################
# Utility functions.
######################################################################
def dump(value, file):
    """Pickles the state of the object (`value`) into the passed file
    (or file name).
    """
    f = _get_file_write(file)
    try:
        StatePickler().dump(value, f)
    finally:
        f.flush()
        if f is not file:
            f.close()
