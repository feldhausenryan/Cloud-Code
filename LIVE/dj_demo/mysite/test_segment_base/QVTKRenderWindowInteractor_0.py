#-----------------------------------------------------------------------
def QVTKRenderWidgetConeExample():
    """A simple example that uses the QVTKRenderWindowInteractor
    class.  """
    # every QT app needs an app
    app = qt.QApplication(['QVTKRenderWindowInteractor'])
    # create the widget
    widget = QVTKRenderWindowInteractor()
    widget.Initialize()
    widget.Start()
    # if you dont want the 'q' key to exit comment this.
    widget.AddObserver("ExitEvent", lambda o, e, a=app: a.quit())
    ren = vtk.vtkRenderer()
    widget.GetRenderWindow().AddRenderer(ren)
    cone = vtk.vtkConeSource()
    cone.SetResolution(8)
    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())
    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    ren.AddActor(coneActor)
    # show the widget
    widget.show()
    # close the application when window is closed
    app.setMainWidget(widget)
    # start event processing
    app.exec_loop()
