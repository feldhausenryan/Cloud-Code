"""
try:
    from errno import EINVAL
except ImportError:
    EINVAL = 22

__all__ = ["StringIO"]

def _complain_ifclosed(closed):
    if closed:
        raise ValueError, "I/O operation on closed file"

class StringIO:
    """class StringIO([buffer])

    When a StringIO object is created, it can be initialized to an existing
    string by passing the string to the constructor. If no string is given,
    the StringIO will start empty.

    The StringIO object can accept either Unicode or 8-bit strings, but
    mixing the two may take some care. If both are used, 8-bit strings that
    cannot be interpreted as 7-bit ASCII (that use the 8th bit) will cause
    a UnicodeError to be raised when getvalue() is called.
    """
    def __init__(self, buf = ''):
        # Force self.buf to be a string or unicode
        if not isinstance(buf, basestring):
            buf = str(buf)
        self.buf = buf
        self.len = len(buf)
        self.buflist = []
        self.pos = 0
        self.closed = False
        self.softspace = 0
