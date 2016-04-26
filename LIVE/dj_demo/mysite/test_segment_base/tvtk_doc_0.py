################################################################################
# Utility functions.
################################################################################
def get_tvtk_class_names():
    """Returns 4 lists:
     1. A list of all the TVTK class names that are not abstract.
     2. A list of the TVTK sources (have only outputs and no inputs)
     3. A list of the TVTK filters (both inputs and outputs)
     4. A list of the TVTK sinks (only inputs and no outputs)
    """
    # Shut of VTK warnings for the time being.
    o = vtk.vtkObject
    w = o.GetGlobalWarningDisplay()
    o.SetGlobalWarningDisplay(0) # Turn it off.
    all = []
    src = []
    filter = []
    sink = []
    for name in dir(vtk):
        if name.startswith('vtk') and not name.startswith('vtkQt'):
            klass = getattr(vtk, name)
            try:
                c = klass()
            except TypeError:
                continue
            tvtk_name = get_tvtk_name(name)
            all.append(tvtk_name)
            has_input = has_output = False
            if hasattr(klass, 'GetNumberOfInputPorts'):
                if c.GetNumberOfInputPorts() > 0:
                    has_input = True
            if hasattr(klass, 'GetNumberOfOutputPorts'):
                if c.GetNumberOfOutputPorts() > 0:
                    has_output = True
            if has_input:
                if has_output:
                    filter.append(tvtk_name)
                else:
                    sink.append(tvtk_name)
            elif has_output:
                src.append(tvtk_name)
    o.SetGlobalWarningDisplay(w)
    result = (all, src, filter, sink)
    for x in result:
        x.sort()
    return result
