# Factory function
def new(nbits, prefix=b(""), suffix=b(""), initial_value=1, overflow=0, little_endian=False, allow_wraparound=False, disable_shortcut=False):
    """Create a stateful counter block function suitable for CTR encryption modes.
    Each call to the function returns the next counter block.
    Each counter block is made up by three parts::
      prefix || counter value || postfix
    The counter value is incremented by one at each call.
    :Parameters:
      nbits : integer
        Length of the desired counter, in bits. It must be a multiple of 8.
      prefix : byte string
        The constant prefix of the counter block. By default, no prefix is
        used.
      suffix : byte string
        The constant postfix of the counter block. By default, no suffix is
        used.
      initial_value : integer
        The initial value of the counter. Default value is 1.
      little_endian : boolean
        If True, the counter number will be encoded in little endian format.
        If False (default), in big endian format.
      allow_wraparound : boolean
        If True, the function will raise an *OverflowError* exception as soon
        as the counter wraps around. If False (default), the counter will
        simply restart from zero.
      disable_shortcut : boolean
        If True, do not make ciphers from `Crypto.Cipher` bypass the Python
        layer when invoking the counter block function.
        If False (default), bypass the Python layer.
    :Returns:
      The counter block function.
    """
    # Sanity-check the message size
    (nbytes, remainder) = divmod(nbits, 8)
    if remainder != 0:
        # In the future, we might support arbitrary bit lengths, but for now we don't.
        raise ValueError("nbits must be a multiple of 8; got %d" % (nbits,))
    if nbytes < 1:
        raise ValueError("nbits too small")
    elif nbytes > 0xffff:
        raise ValueError("nbits too large")
    initval = _encode(initial_value, nbytes, little_endian)
    if little_endian:
        return _counter._newLE(bstr(prefix), bstr(suffix), initval, allow_wraparound=allow_wraparound, disable_shortcut=disable_shortcut)
    else:
        return _counter._newBE(bstr(prefix), bstr(suffix), initval, allow_wraparound=allow_wraparound, disable_shortcut=disable_shortcut)
