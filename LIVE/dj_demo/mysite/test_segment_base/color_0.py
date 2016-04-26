# fixme: This should move into enable.
def wx_to_enable_color(color):
    """ Convert a wx color spec. to an enable color spec. """
    enable_color = array((1.0,1.0,1.0,1.0))
    enable_color[:3] = asarray(color.Get())/255.
    return tuple(enable_color)
