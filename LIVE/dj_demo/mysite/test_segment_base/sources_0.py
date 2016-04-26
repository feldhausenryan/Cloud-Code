######################################################################
# Utility functions
######################################################################
def get_scene(mayavi):
    """Given a mayavi script instance, get the current scene.  If none
    is available create a new one.
    """
    s = mayavi.engine.current_scene
    if s is None:
        mayavi.engine.new_scene()
        s = mayavi.engine.current_scene
    return s
