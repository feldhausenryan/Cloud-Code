#----------------------------------------------------------------------------
def QVTKRenderWidgetConeExample():
    """Like it says, just a simple example
    """
    # every QT app needs an app
    app = QApplication(['QVTKRenderWidget'])
    # create the widget
    widget = QVTKRenderWidget()
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
    qApp.setMainWidget(widget)
    # start event processing
    app.exec_loop()
