# Table description
# -----------------
def append_columns(classdict, shape=()):
    """
    Append a ``Col`` of each PyTables data type to the `classdict`.
    A column of a certain TYPE gets called ``c_TYPE``.  The number of
    added columns is returned.
    """
    heavy = common.heavy
    for (itype, type_) in enumerate(sorted(type_info.iterkeys())):
        if not heavy and type_ in heavy_types:
            continue  # skip heavy type in non-heavy mode
        colpos = itype + 1
        colname = 'c_%s' % type_
        if type_ == 'enum':
            base = tables.Atom.from_sctype(sctype_from_type[type_])
            col = tables.EnumCol(enum, enum(0), base, shape=shape, pos=colpos)
        else:
            sctype = sctype_from_type[type_]
            dtype = numpy.dtype((sctype, shape))
            col = tables.Col.from_dtype(dtype, pos=colpos)
        classdict[colname] = col
    ncols = colpos
    return ncols
