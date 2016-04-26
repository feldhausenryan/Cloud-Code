######################################################################
# Test cases.
######################################################################
def main(instantiate_gui=True):
    """Simple test case."""
    from tvtk.tools import ivtk
    v = ivtk.viewer(browser=False, instantiate_gui=instantiate_gui)
    cs = tvtk.ConeSource()
    m = tvtk.PolyDataMapper(input=cs.output)
    a = tvtk.Actor(mapper=m)
    v.scene.add_actor(a)
    v.scene.reset_zoom()
    b = PipelineBrowser(v.scene)
    b.show()
    return v, b, a
