# This is not just a replacement for byte literals
# but works as a general purpose encoder
def b(s, encoding='utf-8'):
    if isinstance(s, unicode):
        return s.encode(encoding)
    return s
