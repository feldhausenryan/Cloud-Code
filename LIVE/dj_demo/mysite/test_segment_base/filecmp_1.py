# Return a copy with items that occur in skip removed.
#
def _filter(flist, skip):
    return list(ifilterfalse(skip.__contains__, flist))
