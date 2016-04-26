# an alternative implementation, which
# happens to run a bit faster for large
# dictionaries on my machine:
def sortedDictValues2(adict):
    keys = adict.keys()
    keys.sort()
    return [adict[key] for key in keys]
