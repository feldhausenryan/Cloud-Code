# python 2.2 dicts don't have pop
def popd(d, *args):
    """
    Should behave like python2.3 pop method; d is a dict
    # returns value for key and deletes item; raises a KeyError if key
    # is not in dict
    val = popd(d, key)
    # returns value for key if key exists, else default.  Delete key,
    # val item if it exists.  Will not raise a KeyError
    val = popd(d, key, default)
    """
    if len(args)==1:
        key = args[0]
        val = d[key]
        del d[key]
    elif len(args)==2:
        key, default = args
        val = d.get(key, default)
        try: del d[key]
        except KeyError: pass
    return val
