# RFC2231-related functions - parameter encoding and decoding
def decode_rfc2231(s):
    """Decode string according to RFC 2231"""
    parts = s.split(TICK, 2)
    if len(parts) <= 2:
        return None, None, s
    return parts
