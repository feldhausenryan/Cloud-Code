# The entire "while 0:" statement is optimized away.  No code
# exists for it, so the line numbers skip directly from "del x"
# to "x = 1".
def arigo_example():
    x = 1
    del x
    while 0:
        pass
    x = 1
