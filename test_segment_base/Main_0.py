# Do this because PyncheWidget.py wants to get at the interpolated docstring
# too, for its Help menu.
def docstring():
    return __doc__ % globals()
