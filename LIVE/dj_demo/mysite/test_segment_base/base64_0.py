# RFC 3548, Base 16 Alphabet specifies uppercase, but hexlify() returns
# lowercase.  The RFC also recommends against accepting input case
# insensitively.
def b16encode(s):
    """Encode a string using Base16.
    s is the string to encode.  The encoded string is returned.
    """
    return binascii.hexlify(s).upper()
