######################################################################
# Utility functions.
######################################################################
def get_last_input(data):
    """Attempts to get the deepest possible data value in the
    pipeline.  Used when probing a selected point."""
    tmp = inp = data
    while tmp:
        try:
            tmp = inp.input
            if tmp:
                inp = tmp
        except AttributeError:
            tmp = None
    return inp
