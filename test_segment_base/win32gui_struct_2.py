# Helpers for the ugly win32 structure packing/unpacking
# XXX - Note that functions using _GetMaskAndVal run 3x faster if they are
# 'inlined' into the function - see PackLVITEM.  If the profiler points at
# _GetMaskAndVal(), you should nuke it (patches welcome once they have been
# tested)
def _GetMaskAndVal(val, default, mask, flag):
    if val is None:
        return mask, default
    else:
        if flag is not None:
            mask |= flag
        return mask, val
