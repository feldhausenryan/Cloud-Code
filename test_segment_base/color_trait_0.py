### Note: Declare the editor to be a function which returns the ColorEditor
# class from traits ui to avoid circular import issues. For backwards
# compatibility with previous Traits versions, the 'editors' folder in Traits
# project declares 'from api import *' in its __init__.py. The 'api' in turn
# can contain classes that have a Color trait which lead to this file getting
# imported. This leads to a circular import when declaring a Color trait.
def get_color_editor(*args, **traits):
    from ..api import ColorEditor
    return ColorEditor(*args, **traits)
