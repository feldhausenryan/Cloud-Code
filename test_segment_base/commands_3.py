# Make command argument from directory and pathname (prefix space, add quotes).
#
def mk2arg(head, x):
    import os
    return mkarg(os.path.join(head, x))
