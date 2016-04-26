#----Globals filter: filter namespace dictionaries (to be edited in DictEditor)
def is_supported(value, check_all=False, filters=None, iterate=True):
    """Return True if the value is supported, False otherwise"""
    assert filters is not None
    if not is_editable_type(value):
        return False
    elif not isinstance(value, filters):
        return False
    elif iterate:
        if isinstance(value, (list, tuple, set)):
            for val in value:
                if not is_supported(val, filters=filters, iterate=check_all):
                    return False
                if not check_all:
                    break
        elif isinstance(value, dict):
            for key, val in value.iteritems():
                if not is_supported(key, filters=filters, iterate=check_all) \
                   or not is_supported(val, filters=filters,
                                       iterate=check_all):
                    return False
                if not check_all:
                    break
    return True
