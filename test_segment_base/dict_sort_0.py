# (IMHO) the simplest approach:
def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]
