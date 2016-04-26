#
# Rework the Python names (so that float and complex and int are consistent
#                            with Python usage)
#
def _set_up_aliases():
    type_pairs = [('complex_', 'cdouble'),
                  ('int0', 'intp'),
                  ('uint0', 'uintp'),
                  ('single', 'float'),
                  ('csingle', 'cfloat'),
                  ('singlecomplex', 'cfloat'),
                  ('float_', 'double'),
                  ('intc', 'int'),
                  ('uintc', 'uint'),
                  ('int_', 'long'),
                  ('uint', 'ulong'),
                  ('cfloat', 'cdouble'),
                  ('longfloat', 'longdouble'),
                  ('clongfloat', 'clongdouble'),
                  ('longcomplex', 'clongdouble'),
                  ('bool_', 'bool'),
                  ('unicode_', 'unicode'),
                  ('object_', 'object')]
    if sys.version_info[0] >= 3:
        type_pairs.extend([('bytes_', 'string'),
                           ('str_', 'unicode'),
                           ('string_', 'string')])
    else:
        type_pairs.extend([('str_', 'string'),
                           ('string_', 'string'),
                           ('bytes_', 'string')])
    for alias, t in type_pairs:
        allTypes[alias] = allTypes[t]
        sctypeDict[alias] = sctypeDict[t]
    # Remove aliases overriding python types and modules
    to_remove = ['ulong', 'object', 'unicode', 'int', 'long', 'float',
                 'complex', 'bool', 'string', 'datetime', 'timedelta']
    if sys.version_info[0] >= 3:
        # Py3K
        to_remove.append('bytes')
        to_remove.append('str')
        to_remove.remove('unicode')
        to_remove.remove('long')
    for t in to_remove:
        try:
            del allTypes[t]
            del sctypeDict[t]
        except KeyError:
            pass
