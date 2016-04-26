#------------------------------------------------------------------------------
# Layout Helper Functions and Objects
#------------------------------------------------------------------------------
def horizontal(*items, **config):
    """ Create a DeferredConstraints object composed of horizontal
    abutments for the given sequence of items.
    """
    return AbutmentHelper('horizontal', *items, **config)
