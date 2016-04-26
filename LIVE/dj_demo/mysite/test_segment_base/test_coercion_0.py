# avoid testing platform fp quirks
def format_result(value):
    if isinstance(value, complex):
        return '(%s + %sj)' % (format_float(value.real),
                               format_float(value.imag))
    elif isinstance(value, float):
        return format_float(value)
    return str(value)
