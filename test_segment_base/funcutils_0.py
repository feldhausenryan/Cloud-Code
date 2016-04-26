# For backwards compatibility:
def GridFunc(f, xvals, yvals, **keyw):
    return compute_GridData(xvals, yvals, f, **keyw)
