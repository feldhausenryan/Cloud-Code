#----Display <--> Value
def value_to_display(value, truncate=False,
                     trunc_len=80, minmax=False, collvalue=True):
    """Convert value for display purpose"""
    if minmax and isinstance(value, (ndarray, MaskedArray)):
        if value.size == 0:
            return repr(value)
        try:
            return 'Min: %r\nMax: %r' % (value.min(), value.max())
        except TypeError:
            pass
        except ValueError:
            # Happens when one of the array cell contains a sequence
            pass
    if isinstance(value, Image):
        return '%s  Mode: %s' % (address(value), value.mode)
    if not isinstance(value, (str, unicode)):
        if isinstance(value, (list, tuple, dict, set)) and not collvalue:            
            value = address(value)
        else:
            value = repr(value)
    if truncate and len(value) > trunc_len:
        value = value[:trunc_len].rstrip() + ' ...'
    return value
