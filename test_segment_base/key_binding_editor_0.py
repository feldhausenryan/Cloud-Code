# Callable which returns the editor to use in the ui.
def key_binding_editor(*args, **traits):
    return toolkit_object('key_binding_editor:KeyBindingEditor')(*args,
                                                                 **traits)
