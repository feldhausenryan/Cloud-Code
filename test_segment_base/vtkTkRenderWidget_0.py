#----------------------------------------------------------------------------
def vtkRenderWidgetConeExample():
    """Like it says, just a simple example
    """
    # create root window
    root = Tkinter.Tk()
    # create vtkTkRenderWidget
    pane = vtkTkRenderWidget(root,width=300,height=300)
    ren = vtk.vtkRenderer()
    pane.GetRenderWindow().AddRenderer(ren)
    cone = vtk.vtkConeSource()
    cone.SetResolution(8)
    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())
    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    ren.AddActor(coneActor)
    # pack the pane into the tk root
    pane.pack()
    # start the tk mainloop
    root.mainloop()
