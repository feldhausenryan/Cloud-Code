""" codecs -- Python Codec Registry, API and helpers.


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""#"

import __builtin__, sys

### Registry and builtin stateless codec functions

try:
    from _codecs import *
except ImportError, why:
    raise SystemError('Failed to load the builtin codecs: %s' % why)

__all__ = ["register", "lookup", "open", "EncodedFile", "BOM", "BOM_BE",
           "BOM_LE", "BOM32_BE", "BOM32_LE", "BOM64_BE", "BOM64_LE",
           "BOM_UTF8", "BOM_UTF16", "BOM_UTF16_LE", "BOM_UTF16_BE",
           "BOM_UTF32", "BOM_UTF32_LE", "BOM_UTF32_BE",
           "strict_errors", "ignore_errors", "replace_errors",
           "xmlcharrefreplace_errors",
           "register_error", "lookup_error"]

### Constants

#
# Byte Order Mark (BOM = ZERO WIDTH NO-BREAK SPACE = U+FEFF)
# and its possible byte string values
# for UTF8/UTF16/UTF32 output and little/big endian machines
#

# UTF-8
BOM_UTF8 = '\xef\xbb\xbf'

# UTF-16, little endian
BOM_LE = BOM_UTF16_LE = '\xff\xfe'

# UTF-16, big endian
BOM_BE = BOM_UTF16_BE = '\xfe\xff'

# UTF-32, little endian
BOM_UTF32_LE = '\xff\xfe\x00\x00'

# UTF-32, big endian
BOM_UTF32_BE = '\x00\x00\xfe\xff'

if sys.byteorder == 'little':

    # UTF-16, native endianness
    BOM = BOM_UTF16 = BOM_UTF16_LE

    # UTF-32, native endianness
    BOM_UTF32 = BOM_UTF32_LE

else:

    # UTF-16, native endianness
    BOM = BOM_UTF16 = BOM_UTF16_BE

    # UTF-32, native endianness
    BOM_UTF32 = BOM_UTF32_BE

# Old broken names (don't use in new code)
BOM32_LE = BOM_UTF16_LE
BOM32_BE = BOM_UTF16_BE
BOM64_LE = BOM_UTF32_LE
BOM64_BE = BOM_UTF32_BE


### Codec base classes (defining the API)

class CodecInfo(tuple):

    def __new__(cls, encode, decode, streamreader=None, streamwriter=None,
        incrementalencoder=None, incrementaldecoder=None, name=None):
        self = tuple.__new__(cls, (encode, decode, streamreader, streamwriter))
        self.name = name
        self.encode = encode
        self.decode = decode
        self.incrementalencoder = incrementalencoder
        self.incrementaldecoder = incrementaldecoder
        self.streamwriter = streamwriter
        self.streamreader = streamreader
        return self

    def __repr__(self):
        return "<%s.%s object for encoding %s at 0x%x>" % (self.__class__.__module__, self.__class__.__name__, self.name, id(self))

class Codec:

    """ Defines the interface for stateless encoders/decoders.

        The .encode()/.decode() methods may use different error
        handling schemes by providing the errors argument. These
        string values are predefined:

         'strict' - raise a ValueError error (or a subclass)
         'ignore' - ignore the character and continue with the next
         'replace' - replace with a suitable replacement character;
                    Python will use the official U+FFFD REPLACEMENT
                    CHARACTER for the builtin Unicode codecs on
                    decoding and '?' on encoding.
         'xmlcharrefreplace' - Replace with the appropriate XML
                               character reference (only for encoding).
         'backslashreplace'  - Replace with backslashed escape sequences
                               (only for encoding).

        The set of allowed values can be extended via register_error.

    """
    def encode(self, input, errors='strict'):
        """ Encodes the object input and returns a tuple (output
            object, length consumed).
            errors defines the error handling to apply. It defaults to
            'strict' handling.
            The method may not store state in the Codec instance. Use
            StreamCodec for codecs which have to keep state in order to
            make encoding/decoding efficient.
            The encoder must be able to handle zero length input and
            return an empty object of the output object type in this
            situation.
        """
        raise NotImplementedError
