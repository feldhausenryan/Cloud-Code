######################################################################
# Array conversion functions.
######################################################################
def get_vtk_array_type(numeric_array_type):
    """Returns a VTK typecode given a numpy array."""
    # This is a Mapping from numpy array types to VTK array types.
    _arr_vtk = {numpy.dtype(numpy.character):vtkConstants.VTK_UNSIGNED_CHAR,
                numpy.dtype(numpy.uint8):vtkConstants.VTK_UNSIGNED_CHAR,
                numpy.dtype(numpy.uint16):vtkConstants.VTK_UNSIGNED_SHORT,
                numpy.dtype(numpy.int8):vtkConstants.VTK_CHAR,
                numpy.dtype(numpy.int16):vtkConstants.VTK_SHORT,
                numpy.dtype(numpy.int32):vtkConstants.VTK_INT,
                numpy.dtype(numpy.uint32):vtkConstants.VTK_UNSIGNED_INT,
                numpy.dtype(numpy.float32):vtkConstants.VTK_FLOAT,
                numpy.dtype(numpy.float64):vtkConstants.VTK_DOUBLE,
                numpy.dtype(numpy.complex64):vtkConstants.VTK_FLOAT,
                numpy.dtype(numpy.complex128):vtkConstants.VTK_DOUBLE,
                }
    _extra = {numpy.dtype(ID_TYPE_CODE):vtkConstants.VTK_ID_TYPE,
              numpy.dtype(ULONG_TYPE_CODE):vtkConstants.VTK_UNSIGNED_LONG,
              numpy.dtype(LONG_TYPE_CODE):vtkConstants.VTK_LONG,
             }
    for t in _extra:
        if t not in _arr_vtk:
            _arr_vtk[t] = _extra[t]
    try:
        return _arr_vtk[numeric_array_type]
    except KeyError:
        for key in _arr_vtk:
            if numpy.issubdtype(numeric_array_type, key):
                return _arr_vtk[key]
    raise TypeError, "Couldn't translate array's type to VTK"
