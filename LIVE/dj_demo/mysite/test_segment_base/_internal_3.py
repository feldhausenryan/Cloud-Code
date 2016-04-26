# Given an array with fields and a sequence of field names
# construct a new array with just those fields copied over
def _index_fields(ary, fields):
    from multiarray import empty, dtype, array
    dt = ary.dtype
    names = [name for name in fields if name in dt.names]
    formats = [dt.fields[name][0] for name in fields if name in dt.names]
    offsets = [dt.fields[name][1] for name in fields if name in dt.names]
    view_dtype = {'names':names, 'formats':formats, 'offsets':offsets, 'itemsize':dt.itemsize}
    view = ary.view(dtype=view_dtype)
    # Return a copy for now until behavior is fully deprecated
    # in favor of returning view
    copy_dtype = {'names':view_dtype['names'], 'formats':view_dtype['formats']}
    return array(view, dtype=copy_dtype, copy=True)
