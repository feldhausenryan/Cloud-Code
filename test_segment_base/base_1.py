# These are taken from Chaco 1.0's datamapper and subdivision_cells modules.
# TODO: Write unit tests for these!
def right_shift(ary, newval):
    "Returns a right-shifted version of *ary* with *newval* inserted on the left."
    return concatenate([[newval], ary[:-1]])
