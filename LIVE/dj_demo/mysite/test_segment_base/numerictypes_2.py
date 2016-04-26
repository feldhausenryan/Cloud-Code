# Find a data-type that all data-types in a list can be coerced to
def _can_coerce_all(dtypelist, start=0):
    N = len(dtypelist)
    if N == 0:
        return None
    if N == 1:
        return dtypelist[0]
    thisind = start
    while thisind < __len_test_types:
        newdtype = dtype(__test_types[thisind])
        numcoerce = len([x for x in dtypelist if newdtype >= x])
        if numcoerce == N:
            return newdtype
        thisind += 1
    return None
