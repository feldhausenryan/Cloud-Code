#clipmode is ignored if axis is not an integer
def take(array, indices, axis=0, outarr=None, clipmode=RAISE):
    array = np.asarray(array)
    if isinstance(axis, (int, long, np.integer)):
        res = array.take(indices, axis, outarr, clipmode)
        if outarr is None:
            return res
        return
    else:
        def_axes = range(array.ndim)
        for x in axis:
            def_axes.remove(x)
        axis = list(axis) + def_axes
        work = array.transpose(axis)
        res = work[indices]
        if outarr is None:
            return res
        outarr[...] = res
        return
