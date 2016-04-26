##########################################################################
# Helper functions
##########################################################################
def get_mayavi_script_instance():
    """Return the mayavi Script instance from the first available set of
    envisage engines registered in the registry.
    """
    from mayavi.core.registry import registry
    from mayavi.plugins.envisage_engine import EnvisageEngine
    from mayavi.plugins.script import Script
    for name, engine in registry.engines.iteritems():
        if isinstance(engine, EnvisageEngine):
            return engine.window.get_service(Script)
    return
