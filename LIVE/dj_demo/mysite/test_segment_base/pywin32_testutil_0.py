# The test suite has lots of string constants containing binary data, but
# the strings are used in various "bytes" contexts.
def str2bytes(sval):
    if sys.version_info < (3,0) and isinstance(sval, str):
        sval = sval.decode("latin1")
    return sval.encode("latin1")
