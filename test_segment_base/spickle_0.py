######################################################################
# Utility functions.
######################################################################
def get_state(obj):
    """Return a State object given an object.  Useful for testing."""
    str = dumps(obj)
    return StateUnpickler(StringIO(str)).load()
