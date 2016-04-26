#--------------------------------------------------------------------
def wxVTKRenderWindowInteractorConeExample():
    """Like it says, just a simple example
    """
    # every wx app needs an app
    app = wx.PySimpleApp()
    # create the top-level frame, sizer and wxVTKRWI
    frame = wx.Frame(None, -1, "wxVTKRenderWindowInteractor", size=(400,400))
    widget = wxVTKRenderWindowInteractor(frame, -1)
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(widget, 1, wx.EXPAND)
    frame.SetSizer(sizer)
    frame.Layout()
    # It would be more correct (API-wise) to call widget.Initialize() and
    # widget.Start() here, but Initialize() calls RenderWindow.Render().
    # That Render() call will get through before we can setup the
    # RenderWindow() to render via the wxWidgets-created context; this
    # causes flashing on some platforms and downright breaks things on
    # other platforms.  Instead, we call widget.Enable().  This means
    # that the RWI::Initialized ivar is not set, but in THIS SPECIFIC CASE,
    # that doesn't matter.
    widget.Enable(1)
    widget.AddObserver("ExitEvent", lambda o,e,f=frame: f.Close())
    ren = vtk.vtkRenderer()
    widget.GetRenderWindow().AddRenderer(ren)
    cone = vtk.vtkConeSource()
    cone.SetResolution(8)
    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInput(cone.GetOutput())
    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    ren.AddActor(coneActor)
    # show the window
    frame.Show()
    app.MainLoop()
