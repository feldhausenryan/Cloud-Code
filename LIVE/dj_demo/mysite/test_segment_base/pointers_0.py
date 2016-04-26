# create buffer of given size and return it for future reference
# keep a per-context weakref around to allow us to return the original
# array we returned IFF the user has kept a reference as well...
def glSelectBuffer( size, buffer = None ):
    """Create a selection buffer of the given size
    """
    if buffer is None:
        buffer = arrays.GLuintArray.zeros( (size,) )
    simple.glSelectBuffer( size, buffer )
    contextdata.setValue( simple.GL_SELECTION_BUFFER_POINTER, buffer )
    return buffer
