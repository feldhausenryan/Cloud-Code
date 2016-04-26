# assumes file pointer is immediately
#  after the 'fmt ' id
def _read_fmt_chunk(fid):
    if _big_endian:
        fmt = '>'
    else:
        fmt = '<'
    res = struct.unpack(fmt+'ihHIIHH',fid.read(20))
    size, comp, noc, rate, sbytes, ba, bits = res
    if (comp != 1 or size > 16):
        warnings.warn("Unfamiliar format bytes", WavFileWarning)
        if (size>16):
            fid.read(size-16)
    return size, comp, noc, rate, sbytes, ba, bits
