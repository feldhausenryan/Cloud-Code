#----------------------------------------------------------------------------
def wxVTKRenderWindowConeExample():
    """Like it says, just a simple example.
    """
    # every wx app needs an app
    app = wx.PySimpleApp()
    # create the widget
    frame = wx.Frame(None, -1, "wxVTKRenderWindow", size=(400,400))
    widget = wxVTKRenderWindow(frame, -1)
    ren = vtk.vtkRenderer()
    widget.GetRenderWindow().AddRenderer(ren)
    cone = vtk.vtkConeSource()
    cone.SetResolution(8)
    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())
    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    ren.AddActor(coneActor)
    # show the window
    frame.Show()
    app.MainLoop()
