##########################################################################
# Traits UI factory functions.
##########################################################################
def gradient_editor_factory(parent, trait_editor):
    """This is a factory function for `traitsui.CustomEditor` and allows us to
    use the `wxGradientEditorWidget` or `QGradientEditorWidget` as a traits 
    UI editor.
    """
    tvtk_obj = getattr(trait_editor.object, trait_editor.name)
    if ETSConfig.toolkit == 'wx':
        from wx_gradient_editor import wxGradientEditorWidget
        widget = wxGradientEditorWidget(parent, tvtk_obj)
    elif ETSConfig.toolkit == 'qt4':
        from qt_gradient_editor import QGradientEditorWidget
        widget = QGradientEditorWidget(None, tvtk_obj)
    else:
        msg = 'Toolkit %s does not implement gradient_editors.'%ETSConfig.toolkit
        raise NotImplementedError(msg)
    return widget
