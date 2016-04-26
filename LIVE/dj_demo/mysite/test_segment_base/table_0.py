# TODO: Allow tbtype to be either a string or a class; perhaps eventually
# replace this with separate functions for creating tables (possibly in the
# form of a classmethod)  See ticket #60
def new_table(input, header=None, nrows=0, fill=False, tbtype='BinTableHDU'):
    """
    Create a new table from the input column definitions.
    Warning: Creating a new table using this method creates an in-memory *copy*
    of all the column arrays in the input.  This is because if they are
    separate arrays they must be combined into a single contiguous array.
    If the column data is already in a single contiguous array (such as an
    existing record array) it may be better to create a BinTableHDU instance
    directly.  See the PyFITS documentation for more details.
    Parameters
    ----------
    input : sequence of Column or ColDefs objects
        The data to create a table from.
    header : Header instance
        Header to be used to populate the non-required keywords.
    nrows : int
        Number of rows in the new table.
    fill : bool
        If `True`, will fill all cells with zeros or blanks.  If
        `False`, copy the data from input, undefined cells will still
        be filled with zeros/blanks.
    tbtype : str
        Table type to be created ("BinTableHDU" or "TableHDU").
    """
    # construct a table HDU
    # TODO: Something needs to be done about this as part of #60....
    hdu = eval(tbtype)(header=header)
    if isinstance(input, ColDefs):
        # NOTE: This previously raised an error if the tbtype didn't match the
        # tbtype of the input ColDefs. This should no longer be necessary, but
        # just beware.
        columns = hdu.columns = ColDefs(input)
    elif isinstance(input, FITS_rec):  # input is a FITS_rec
        # Create a new ColDefs object from the input FITS_rec's ColDefs
        # object and assign it to the ColDefs attribute of the new hdu.
        columns = hdu.columns = ColDefs(input._coldefs, tbtype)
    else:  # input is a list of Columns or possibly a recarray
        # Create a new ColDefs object from the input list of Columns and
        # assign it to the ColDefs attribute of the new hdu.
        columns = hdu.columns = ColDefs(input, tbtype)
    # read the delayed data
    for idx in range(len(columns)):
        arr = columns._arrays[idx]
        if isinstance(arr, Delayed):
            if arr.hdu.data is None:
                columns._arrays[idx] = None
            else:
                columns._arrays[idx] = np.rec.recarray.field(arr.hdu.data,
                                                             arr.field)
    # use the largest column shape as the shape of the record
    if nrows == 0:
        for arr in columns._arrays:
            if (arr is not None):
                dim = arr.shape[0]
            else:
                dim = 0
            if dim > nrows:
                nrows = dim
    if tbtype == 'TableHDU':
        columns = hdu.columns = _ASCIIColDefs(hdu.columns)
        _itemsize = columns.spans[-1] + columns.starts[-1] - 1
        dtype = {}
        for j in range(len(columns)):
            data_type = 'S' + str(columns.spans[j])
            dtype[columns.names[j]] = (data_type, columns.starts[j] - 1)
        hdu.data = np.rec.array((' ' * _itemsize * nrows).encode('ascii'),
                                dtype=dtype, shape=nrows).view(FITS_rec)
        hdu.data.setflags(write=True)
    else:
        formats = ','.join(columns._recformats)
        hdu.data = np.rec.array(None, formats=formats,
                                names=columns.names,
                                shape=nrows).view(FITS_rec)
    hdu.data._coldefs = hdu.columns
    hdu.data.formats = hdu.columns.formats
    # Populate data to the new table from the ndarrays in the input ColDefs
    # object.
    for idx in range(len(columns)):
        # For each column in the ColDef object, determine the number
        # of rows in that column.  This will be either the number of
        # rows in the ndarray associated with the column, or the
        # number of rows given in the call to this function, which
        # ever is smaller.  If the input FILL argument is true, the
        # number of rows is set to zero so that no data is copied from
        # the original input data.
        arr = columns._arrays[idx]
        recformat = columns._recformats[idx]
        if arr is None:
            size = 0
        else:
            size = len(arr)
        n = min(size, nrows)
        if fill:
            n = 0
        # Get any scale factors from the FITS_rec
        scale, zero, bscale, bzero, dim = hdu.data._get_scale_factors(idx)[3:]
        field = np.rec.recarray.field(hdu.data, idx)
        if n > 0:
            # Only copy data if there is input data to copy
            # Copy all of the data from the input ColDefs object for this
            # column to the new FITS_rec data array for this column.
            if isinstance(recformat, _FormatX):
                # Data is a bit array
                if arr[:n].shape[-1] == recformat._nx:
                    _wrapx(arr[:n], field[:n], recformat._nx)
                else:
                    # from a table parent data, just pass it
                    field[:n] = arr[:n]
            elif isinstance(recformat, _FormatP):
                hdu.data._convert[idx] = _makep(arr[:n], field, recformat,
                                                nrows=nrows)
            elif recformat[-2:] == FITS2NUMPY['L'] and arr.dtype == bool:
                # column is boolean
                field[:n] = np.where(arr == False, ord('F'), ord('T'))
            else:
                if tbtype == 'TableHDU':
                    # string no need to convert,
                    if isinstance(arr, chararray.chararray):
                        field[:n] = arr[:n]
                    else:
                        hdu.data._convert[idx] = \
                                np.zeros(nrows, dtype=arr.dtype)
                        if scale or zero:
                            arr = arr.copy()
                        if scale:
                            arr *= bscale
                        if zero:
                            arr += bzero
                        hdu.data._convert[idx][:n] = arr[:n]
                else:
                    field[:n] = arr[:n]
        if n < nrows:
            # If there are additional rows in the new table that were not
            # copied from the input ColDefs object, initialize the new data
            if tbtype == 'BinTableHDU':
                if isinstance(field, np.ndarray):
                    field[n:] = -bzero / bscale
                else:
                    field[n:] = ''
            else:
                field[n:] = ' ' * hdu.data._coldefs.spans[idx]
    # Update the HDU header to match the data
    hdu.update()
    # Make the ndarrays in the Column objects of the ColDefs object of the HDU
    # reference the same ndarray as the HDU's FITS_rec object.
    for idx in range(len(columns)):
        hdu.columns[idx].array = hdu.data.field(idx)
    # Delete the _arrays attribute so that it is recreated to point to the
    # new data placed in the column objects above
    del hdu.columns._arrays
    return hdu
