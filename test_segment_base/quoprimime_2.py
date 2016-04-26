# Header decoding is done a bit differently
def header_decode(s):
    """Decode a string encoded with RFC 2045 MIME header `Q' encoding.
    This function does not parse a full MIME header value encoded with
    quoted-printable (like =?iso-8895-1?q?Hello_World?=) -- please use
    the high level email.header class for that functionality.
    """
    s = s.replace('_', ' ')
    return re.sub(r'=[a-fA-F0-9]{2}', _unquote_match, s)
