# fixme: We'd like to use a callable instance for the listener so that we
# can maintain state, but traits barfs trying to determine the signature 8^()
def create_listener():
    """ Create a listener for testing trait notifications. """
    def listener(obj, trait_name, old, new):
        listener.obj        = obj
        listener.trait_name = trait_name
        listener.new        = new
        listener.old        = old
        listener.called     += 1
        return
    listener.initialize = lambda : initialize_listener(listener)
    return initialize_listener(listener)
