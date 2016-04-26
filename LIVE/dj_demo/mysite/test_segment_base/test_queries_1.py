# Non-indexed queries: ``[SB][SM]TDTestCase``, where:
#
# 1. S is for small and B is for big size table.
#    Sizes are listed in `table_sizes`.
# 2. S is for scalar and M for multidimensional columns.
#    Dimensionalities are listed in `table_ndims`.
def niclassdata():
    for size in table_sizes:
        heavy = size in heavy_table_sizes
        for ndim in table_ndims:
            classname = '%s%sTDTestCase' % (size[0], ndim[0])
            cbasenames = ( '%sNITableMixin' % size, '%sTableMixin' % ndim,
                           'TableDataTestCase' )
            classdict = dict(heavy=heavy)
            yield (classname, cbasenames, classdict)
