######################################################################
# Utility functions.
######################################################################
def deref_vtk(obj):
    """Dereferences the VTK object from the object if possible."""
    if isinstance(obj, TVTKBase):
        return obj._vtk_obj
    else:
        return obj
