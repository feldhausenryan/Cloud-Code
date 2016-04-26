######################################################################
# Utility functions.
######################################################################
def viewer(browser=True, instantiate_gui=False):
    """Creates an IVTK instance, opens the window and returns the
    embedded scene inside it.  This is useful from an IPython/vanilla
    Python shell.  It returns the viewer window instance.
    Parameters
    ----------
    - browser : `bool` (default, True)
      If True, creates an IVTK scene with an embedded PipelineBrowser.
      If False, does not create it.
    - instantiate_gui : `bool` (default: False)
      If True, create an instance of GUI().  This is useful when this
      function is invoked from within an IPython shell.  OTOH, if this
      is called from within a wxPython app (or with ipython -wthread)
      you don't want to start another GUI instance.
    """
    if instantiate_gui:
        gui = GUI()
    if browser:
        v = IVTKWithBrowser(size=(600,600))
    else:
        v = IVTK(size=(600,600))
    v.open()
    return v
