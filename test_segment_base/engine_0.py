######################################################################
# Utility functions.
######################################################################
def _id_generator():
    """Returns a sequence of numbers for the title of the scene
    window."""
    n = 1
    while True:
        yield(n)
        n += 1
