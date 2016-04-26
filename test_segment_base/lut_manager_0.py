#################################################################
# Utility functions.
#################################################################
def set_lut(vtk_lut, lut_lst):
    """Setup the tvtk.LookupTable (`vtk_lut`) using the passed list of
    lut values."""
    n_col = len(lut_lst)
    vtk_lut.number_of_colors = n_col
    vtk_lut.build()
    for i in range(0, n_col):
        lt = lut_lst[i]
        vtk_lut.set_table_value(i, lt[0], lt[1], lt[2], lt[3])
    return vtk_lut
