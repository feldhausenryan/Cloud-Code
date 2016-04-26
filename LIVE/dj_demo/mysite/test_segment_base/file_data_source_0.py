######################################################################
# Utility functions.
######################################################################
def get_file_list(file_name):
    """ Given a file name, this function treats the file as a part of
    a series of files based on the index of the file and tries to
    determine the list of files in the series.  The file name of a
    file in a time series must be of the form 'some_name[0-9]*.ext'.
    That is the integers at the end of the file determine what part of
    the time series the file belongs to.  The files are then sorted as
    per this index."""
    # The matching is done only for the basename of the file.
    f_dir, f_base = split(file_name)
    # Find the head and tail of the file pattern.
    head = re.sub("[0-9]+[^0-9]*$", "", f_base)
    tail = re.sub("^.*[0-9]+", "", f_base)
    pattern = head+"[0-9]*"+tail
    # Glob the files for the pattern.
    _files = glob(join(f_dir, pattern))
    # A simple function to get the index from the file.
    def _get_index(f, head=head, tail=tail):
        base = split(f)[1]
        result = base.replace(head, '')
        return float(result.replace(tail, ''))
    # Before sorting make sure the files in the globbed series are
    # really part of a timeseries.  This can happen in cases like so:
    # 5_2_1.vtk and 5_2_1s.vtk will be globbed but 5_2_1s.vtk is
    # obviously not a valid time series file.
    files = []
    for x in _files:
        try:
            _get_index(x)
        except ValueError:
            pass
        else:
            files.append(x)
    # Sort the globbed files based on the index value.
    def file_sort(x, y):
        x1 = _get_index(x)
        y1 = _get_index(y)
        if x1 > y1:
            return 1
        elif y1 > x1:
            return -1
        else:
            return 0
    files.sort(file_sort)
    return files
