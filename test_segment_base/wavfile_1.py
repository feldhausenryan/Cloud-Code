# assumes file pointer is immediately
#   after the 'data' id
def _read_data_chunk(fid, noc, bits, mmap=False):
    if _big_endian:
        fmt = '>i'
    else:
        fmt = '<i'
    size = struct.unpack(fmt,fid.read(4))[0]
    bytes = bits//8
    if bits == 8:
        dtype = 'u1'
    elif _big_endian:
        dtype = '>i%d' % bytes
    else:
        dtype = '<i%d' % bytes
    if not mmap:
        data = numpy.fromfile(fid, dtype=dtype, count=size//bytes)
    else:
        start = fid.tell()
        data = numpy.memmap(fid, dtype=dtype, mode='c', offset=start,
                            shape=(size//bytes,))
        fid.seek(start + size)
    if noc > 1:
        data = data.reshape(-1,noc)
    return data
