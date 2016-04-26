# convert a normal int to a long int - used to avoid, eg, '1L' for py3k
# friendliness
def ensure_long(int_val):
    if sys.version_info > (3,):
        # py3k - no such thing as a 'long'
        return int_val
    # on py2x, we just use an expression that results in a long
    return 0x100000000-0x100000000+int_val
