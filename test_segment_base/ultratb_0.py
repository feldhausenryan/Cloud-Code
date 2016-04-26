# Utility functions
def inspect_error():
    """Print a message about internal inspect errors.
    These are unfortunately quite common."""
    error('Internal Python error in the inspect module.\n'
          'Below is the traceback from this internal error.\n')
