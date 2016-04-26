# Called in PyArray_DescrConverter function when
#  a dictionary without "names" and "formats"
#  fields is used as a data-type descriptor.
def _usefields(adict, align):
    from multiarray import dtype
    try:
        names = adict[-1]
    except KeyError:
        names = None
    if names is None:
        names, formats, offsets, titles = _makenames_list(adict, align)
    else:
        formats = []
        offsets = []
        titles = []
        for name in names:
            res = adict[name]
            formats.append(res[0])
            offsets.append(res[1])
            if (len(res) > 2):
                titles.append(res[2])
            else:
                titles.append(None)
    return dtype({"names" : names,
                  "formats" : formats,
                  "offsets" : offsets,
                  "titles" : titles}, align)
