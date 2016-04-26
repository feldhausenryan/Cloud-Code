# used when parsing config files
def flag(val):
    """Does the value look like an on/off flag?"""
    if val == 1:
        return True
    elif val == 0:
        return False
    val = str(val)
    if len(val) > 5:
        return False
    return val.upper() in ('1', '0', 'F', 'T', 'TRUE', 'FALSE', 'ON', 'OFF')
