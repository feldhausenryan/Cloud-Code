# Convenience functions for extending the above mappings
def add_charset(charset, header_enc=None, body_enc=None, output_charset=None):
    """Add character set properties to the global registry.
    charset is the input character set, and must be the canonical name of a
    character set.
    Optional header_enc and body_enc is either Charset.QP for
    quoted-printable, Charset.BASE64 for base64 encoding, Charset.SHORTEST for
    the shortest of qp or base64 encoding, or None for no encoding.  SHORTEST
    is only valid for header_enc.  It describes how message headers and
    message bodies in the input charset are to be encoded.  Default is no
    encoding.
    Optional output_charset is the character set that the output should be
    in.  Conversions will proceed from input charset, to Unicode, to the
    output charset when the method Charset.convert() is called.  The default
    is to output in the same character set as the input.
    Both input_charset and output_charset must have Unicode codec entries in
    the module's charset-to-codec mapping; use add_codec(charset, codecname)
    to add codecs the module does not know about.  See the codecs module's
    documentation for more information.
    """
    if body_enc == SHORTEST:
        raise ValueError('SHORTEST not allowed for body_enc')
    CHARSETS[charset] = (header_enc, body_enc, output_charset)
