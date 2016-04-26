# a further slight speed-up on my box
# is to map a bound-method:
def sortedDictValues3(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)
