# Sometimes we want to pass an object that exposes its memory
def ob2memory(ob):
    if sys.version_info < (3,0):
        return buffer(ob)
    # py3k.
    return memoryview(ob)
