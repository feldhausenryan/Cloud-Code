# Define the ColorEditor class
# The function will try to return the toolkit-specific editor factory (located
# in traitsui.<toolkit>.color_editor, and if none is found, the
# ToolkitEditorFactory declared here is returned.
def ColorEditor(*args, **traits):
    """ Returns an instance of the toolkit-specific editor factory declared in
    traitsui.<toolkit>.color_editor. If such an editor factory
    cannot be located, an instance of the abstract ToolkitEditorFactory
    declared in traitsui.editors.color_editor is returned.
    Parameters
    ----------
    \*args, \*\*traits
        arguments and keywords to be passed on to the editor
        factory's constructor.
    """
    try:
        return toolkit_object('color_editor:ToolkitEditorFactory', True)(*args,
                                                                    **traits)
    except:
        return ToolkitEditorFactory(*args, **traits)
