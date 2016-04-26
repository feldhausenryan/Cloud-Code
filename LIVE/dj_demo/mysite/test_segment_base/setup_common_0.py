# Code to detect long double representation taken from MPFR m4 macro
def check_long_double_representation(cmd):
    cmd._check_compiler()
    body = LONG_DOUBLE_REPRESENTATION_SRC % {'type': 'long double'}
    # We need to use _compile because we need the object filename
    src, object = cmd._compile(body, None, None, 'c')
    try:
        type = long_double_representation(pyod(object))
        return type
    finally:
        cmd._clean()
