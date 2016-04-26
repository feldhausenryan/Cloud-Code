# Build a new array from the information in a pickle.
# Note that the name numpy.core._internal._reconstruct is embedded in
# pickles of ndarrays made with NumPy before release 1.0
# so don't remove the name here, or you'll
# break backward compatibilty.
def _reconstruct(subtype, shape, dtype):
    from multiarray import ndarray
    return ndarray.__new__(subtype, shape, dtype)
