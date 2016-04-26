# [].sort
def sort_list(l, cmp=None, key=None, reverse=False):
    try:
        l.sort(cmp, key, reverse)
    except TypeError, e:
        if not str(e).startswith('sort expected at most 1 arguments'):
            raise
        if cmp is None:
            cmp = orig_cmp
        if key is not None:
            # the cmp=cmp parameter is required to get the original comparator
            # into the lambda namespace
            cmp = lambda self, other, cmp=cmp: cmp(key(self), key(other))
        if reverse:
            cmp = lambda self, other, cmp=cmp: -cmp(self,other)
        l.sort(cmp)
