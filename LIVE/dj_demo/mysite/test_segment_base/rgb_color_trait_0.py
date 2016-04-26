### Note: Declare the editor to be a function which returns the RGBColorEditor
# class from traits ui to avoid circular import issues. For backwards
# compatibility with previous Traits versions, the 'editors' folder in Traits
# project declares 'from api import *' in its __init__.py. The 'api' in turn
# can contain classes that have a RGBColor trait which lead to this file getting
# imported. This will lead to a circular import when declaring a RGBColor trait.
def get_rgb_color_editor(*args, **traits):
    from ..editors.rgb_color_editor import ToolkitEditorFactory as RGBColorEditor
    return RGBColorEditor(*args, **traits)
