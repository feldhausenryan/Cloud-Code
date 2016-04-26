# Sometimes we want to pass a string that should explicitly be treated as
# a memory blob.
def str2memory(sval):
    if sys.version_info < (3,0):
        return buffer(sval)
    # py3k.
    return memoryview(sval.encode("latin1"))
