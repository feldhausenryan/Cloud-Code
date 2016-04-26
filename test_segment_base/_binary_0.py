# Input, le = little endian, be = big endian
def i16le(c, o=0):
    return i8(c[o]) | (i8(c[o+1])<<8)
