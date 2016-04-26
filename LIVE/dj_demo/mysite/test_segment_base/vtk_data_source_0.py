######################################################################
# Utility functions.
######################################################################
def write_dataset_to_string(data):
    """Given a dataset, convert the dataset to an ASCII string that can
    be stored for persistence.
    """
    w = tvtk.DataSetWriter(write_to_output_string=1)
    warn = w.global_warning_display
    w.set_input(data)
    w.global_warning_display = 0
    w.update()
    if w.output_string_length == 0:
        # Some VTK versions (5.2) have a bug when writing structured
        # grid datasets and produce empty output.  We work around this
        # by writing to a file and then reading that output.
        w.write_to_output_string = 0
        fh, fname = tempfile.mkstemp('.vtk')
        os.close(fh); os.remove(fname)
        w.file_name = fname
        w.write()
        # Read the data and delete the file.
        sdata = open(fname).read()
        os.remove(fname)
    else:
        sdata = w.output_string
    w.global_warning_display = warn
    return sdata
