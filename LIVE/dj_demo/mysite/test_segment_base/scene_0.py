######################################################################
# Utility functions.
######################################################################
def popup_save(parent=None):
    """Popup a dialog asking for an image name to save the scene to.
    This is used mainly to save a scene in full screen mode. Returns a
    filename, returns empty string if action was cancelled. `parent` is
    the parent widget over which the dialog will be popped up.
    """
    extns = ['*.png', '*.jpg', '*.jpeg', '*.tiff', '*.bmp', '*.ps', '*.eps',
             '*.tex', '*.rib', '*.wrl', '*.oogl', '*.pdf', '*.vrml', '*.obj',
             '*.iv']
    wildcard='|'.join(extns)
    dialog = FileDialog(
        parent = parent, title='Save scene to image',
        action='save as', wildcard=wildcard
    )
    if dialog.open() == OK:
        return dialog.path
    else:
        return ''
