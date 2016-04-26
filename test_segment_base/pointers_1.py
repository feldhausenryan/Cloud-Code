# XXX this belongs in the GL module, not here!
def glGetPointerv( constant ):
    """Retrieve a stored pointer constant"""
    # do we have a cached version of the pointer?
    # get the base pointer from the underlying operation
    vp = ctypes.voidp()
    simple.glGetPointerv( constant, ctypes.byref(vp) )
    current = contextdata.getValue( constant )
    if current is not None:
        if arrays.ArrayDatatype.dataPointer( current ) == vp.value:
            return current
    # XXX should be coercing to the proper type and converting to an array
    return vp
