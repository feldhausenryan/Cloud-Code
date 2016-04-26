# Helper functions
def get_sliced_vars(npvars, start, stop, step):
    npvars_ = {}
    for name, var in npvars.iteritems():
        if hasattr(var, "__len__"):
            npvars_[name] = var[start:stop:step]
        else:
            npvars_[name] = var
    return npvars_
