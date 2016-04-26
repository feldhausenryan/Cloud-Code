# Now the real glReadPixels...
def glReadPixels( x,y,width,height,format,type, array=None, outputType=str ):
    """Read specified pixels from the current display buffer
    x,y,width,height -- location and dimensions of the image to read
        from the buffer
    format -- pixel format for the resulting data
    type -- data-format for the resulting data
    array -- optional array/offset into which to store the value
    outputType -- default (str) provides string output of the
        results iff OpenGL.UNSIGNED_BYTE_IMAGES_AS_STRING is True
        and type == GL_UNSIGNED_BYTE.  Any other value will cause
        output in the default array output format.
    returns the pixel data array in the format defined by the
    format, type and outputType
    """
    x,y,width,height = asInt(x),asInt(y),asInt(width),asInt(height)
    arrayType = arrays.GL_CONSTANT_TO_ARRAY_TYPE[ images.TYPE_TO_ARRAYTYPE.get(type,type) ]
    if array is None:
        array = images.SetupPixelRead( format, (width,height), type )
    else:
        array = arrayType.asArray( array )
    imageData = arrayType.voidDataPointer( array )
    GL_1_1.glReadPixels(
        x,y,width,height,
        format,type,
        imageData
    )
    if outputType is str:
        return images.returnFormat( array, type )
    else:
        return array
