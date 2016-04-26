# Implement the dump and dumps methods so that all traits in a HasTraits object
# get included in the pickle.
def dump(obj, file, protocol=2):
    _flush_traits(obj)
    from cPickle import dump as d
    return d(obj, file, protocol)
