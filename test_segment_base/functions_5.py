#clipmode is ignored if axis is not 0 and array is not 1d
def put(array, indices, values, axis=0, clipmode=RAISE):
    if not isinstance(array, np.ndarray):
        raise TypeError("put only works on subclass of ndarray")
    work = asarray(array)
    if axis == 0:
        if array.ndim == 1:
            work.put(indices, values, clipmode)
        else:
            work[indices] = values
    elif isinstance(axis, (int, long, np.integer)):
        work = work.swapaxes(0, axis)
        work[indices] = values
        work = work.swapaxes(0, axis)
    else:
        def_axes = range(work.ndim)
        for x in axis:
            def_axes.remove(x)
        axis = list(axis)+def_axes
        work = work.transpose(axis)
        work[indices] = values
        work = work.transpose(axis)
