# Indexed queries: ``[ULMF]I[NH]SVXYTestCase``, where:
#
# 1. U is for 'UltraLight', L for 'Light', M for 'Medium', F for 'Full' indexes
# 2. N is for 'Normal', H for 'Heavy' tests
def iclassdata():
    for ckind in ckinds:
        for ctest in normal_tests + heavy_tests:
            classname = '%sI%s%s' % (ckind[0], testlevels[heavy][0], ctest)
            # Uncomment the next one and comment the past one if one
            # don't want to include the methods (testing purposes only)
            ###cbasenames = ( '%sITableMixin' % ckind, "object")
            cbasenames = ( '%sITableMixin' % ckind, ctest)
            classdict = dict(heavy=bool(ctest in heavy_tests))
            yield (classname, cbasenames, classdict)
