# Indexed queries: ``[SMB]I[ulmf]O[01379]TDTestCase``, where:
#
# 1. S is for small, M for medium and B for big size table.
#    Sizes are listed in `itable_sizes`.
# 2. U is for 'ultraLight', L for 'light', M for 'medium', F for 'Full' indexes
#    Index types are listed in `ckinds`.
# 3. 0 to 9 is the desired index optimization level.
#    Optimizations are listed in `itable_optvalues`.
def iclassdata():
    for ckind in ckinds:
        for size in itable_sizes:
            for optlevel in itable_optvalues:
                heavy = ( optlevel in heavy_itable_optvalues
                          or size in heavy_itable_sizes )
                classname = '%sI%sO%dTDTestCase' % (
                    size[0], ckind[0], optlevel)
                cbasenames = ( '%sSTableMixin' % size,
                               '%sITableMixin' % ckind,
                               'ScalarTableMixin',
                               'TableDataTestCase' )
                classdict = dict(heavy=heavy, optlevel=optlevel, indexed=True)
                yield (classname, cbasenames, classdict)
