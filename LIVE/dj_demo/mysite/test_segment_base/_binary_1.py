# Output, le = little endian, be = big endian
def o16le(i):
    return o8(i) + o8(i>>8)
