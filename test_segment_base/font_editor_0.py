# Define the FontEditor class
# The function will try to return the toolkit-specific editor factory (located
# in traitsui.<toolkit>.font_editor, and if none is found, the
# ToolkitEditorFactory declared here is returned.
def FontEditor(*args, **traits):
    """ Returns an instance of the toolkit-specific editor factory declared in
    traitsui.<toolkit>.font_editor. If such an editor factory
    cannot be located, an instance of the abstract ToolkitEditorFactory
    declared in traitsui.editors.font_editor is returned.
    Parameters
    ----------
    \*args, \*\*traits
        arguments and keywords to be passed on to the editor
        factory's constructor.
    """
    try:
       return toolkit_object('font_editor:ToolkitEditorFactory', True)(*args,
                                                                    **traits)
    except Exception, e:
       return ToolkitEditorFactory(*args, **traits)
