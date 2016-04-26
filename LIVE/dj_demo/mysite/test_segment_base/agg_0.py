# !! Temporary until we get the __init__ code in swig fixed.
def init(self, ary_or_size, pix_format="bgra32",
             interpolation="nearest",bottom_up = 1):
    """ When specifying size, it must be a two element tuple.
        Array input is always treated as an image.
        This class handles the polymorphism of the underlying
        template classes for individual pixel formats.
    """
    pix_format_id = pix_format_string_map[pix_format]
    img_depth = pix_format_bytes[pix_format]
    interpolation_id = interp_string_map[interpolation]
    if type(ary_or_size) is tuple:
        width,height = ary_or_size
        ary = zeros((height,width,img_depth),uint8)
        ary[:] = 255
    else:
        ary = ary_or_size
        sh = shape(ary)
        if len(sh) == 2:
            msg = "2D arrays must use a format that is one byte per pixel"
            assert img_depth == 1, msg
        elif len(sh) == 3:
            msg = "Image depth and format are incompatible"
            assert img_depth == sh[2], msg
        else:
            msg = "only 2 or 3 dimensional arrays are supported as images"
            msg += " but got sh=%r" % (sh,)
            raise TypeError, msg
        msg = "Only UnsignedInt8 arrays are supported but got "
        assert ary.dtype == dtype('uint8'), msg + repr(ary.dtype)
    if cvar.ALWAYS_32BIT_WORKAROUND_FLAG:
        if ary.shape[-1] == 3:
            if pix_format not in ('rgb24', 'bgr24'):
                import warnings
                warnings.warn('need to workaround AGG bug since '
                	'ALWAYS_32BIT_WORKAROUND is on, but got unhandled '
                	'format %r' % pix_format)
            else:
                pix_format = '%sa32' % pix_format[:3]
                ary = numpy.dstack([ary, numpy.empty(ary.shape[:2], dtype=uint8)])
                ary[:,:,-1].fill(255)
        pix_format_id = pix_format_string_map[pix_format]
        img_depth = pix_format_bytes[pix_format]
    obj = graphics_context_from_array(ary,pix_format_id,interpolation_id,
                                      bottom_up)
    _swig_setattr(self, GraphicsContextArray, 'this', obj)
    # swig 1.3.28 does not have real thisown, thisown is mapped
    # to this.own() but with previous 'self.this=obj' an
    # attribute 'own' error is raised. Does this workaround
    # work with pre-1.3.28 swig?
    _swig_setattr(self, GraphicsContextArray, 'thisown2', 1)
    self.bmp_array = ary
