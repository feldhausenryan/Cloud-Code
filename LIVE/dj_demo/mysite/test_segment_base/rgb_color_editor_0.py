# Define the RGBColorEditor class
# The function will try to return the toolkit-specific editor factory (located
# in traitsui.<toolkit>.rgb_color_editor, and if none is found, the
# ToolkitEditorFactory declared here is returned.
def RGBColorEditor(*args, **traits):
    """ Returns an instance of the toolkit-specific editor factory declared in
    traitsui.<toolkit>.rgb_color_editor. If such an editor factory
    cannot be located, an instance of the abstract ToolkitEditorFactory
    declared in traitsui.editors.rgb_color_editor is returned.
    Parameters
    ----------
    \*args, \*\*traits
        arguments and keywords to be passed on to the editor
        factory's constructor.
    """
    try:
       return toolkit_object('rgb_color_editor:ToolkitEditorFactory', True)(
                                                            *args, **traits)
    except:
       return ToolkitEditorFactory(*args, **traits)
