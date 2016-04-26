# Callable which returns the editor to use in the ui.
def null_editor(*args, **traits):
    return toolkit_object('null_editor:NullEditor')(*args, **traits)
