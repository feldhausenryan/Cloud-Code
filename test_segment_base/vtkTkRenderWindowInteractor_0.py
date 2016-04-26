#----------------------------------------------------------------------------
def vtkRenderWindowInteractorConeExample():
    """Like it says, just a simple example
    """
    # create root window
    root = Tkinter.Tk()
    # create vtkTkRenderWidget
    pane = vtkTkRenderWindowInteractor(root, width=300, height=300)
    pane.Initialize()
    def quit(obj=root):
        obj.quit()
    pane.AddObserver("ExitEvent", lambda o,e,q=quit: q())
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
    pane.pack(fill='both', expand=1)
    pane.Start()
    # start the tk mainloop
    root.mainloop()
