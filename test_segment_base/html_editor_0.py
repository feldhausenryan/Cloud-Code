# Callable that returns the editor to use in the UI.
def html_editor(*args, **traits):
    return toolkit_object('html_editor:SimpleEditor')(*args, **traits)
