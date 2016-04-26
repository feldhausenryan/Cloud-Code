# Albert's ctypes pattern
def _register_api(lib, api):
    nlib = _ctypes_wrapper()
    for f, (restype, argtypes) in api.items():
        try:
            func = getattr(lib, f)
            func.restype = restype
            func.argtypes = argtypes
            setattr(nlib, f, func)
        except Exception:
            def error_raise(*args):
                raise RuntimeError(
                    'mahotas.freeimage: Function `%s` not found in your'
                    ' version of FreeImage. It might be an older version' % f)
            setattr(nlib, f, error_raise)
    return nlib
