# XXX Deprecated
def SetPointerType(pointer, cls):
    if _pointer_type_cache.get(cls, None) is not None:
        raise RuntimeError("This type already exists in the cache")
    if id(pointer) not in _pointer_type_cache:
        raise RuntimeError("What's this???")
    pointer.set_type(cls)
    _pointer_type_cache[cls] = pointer
    del _pointer_type_cache[id(pointer)]
