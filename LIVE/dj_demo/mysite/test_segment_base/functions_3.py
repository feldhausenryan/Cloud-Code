# taken and adapted directly from numarray
def fromfile(infile, type=None, shape=None, sizing=STRICT,
             typecode=None, dtype=None):
    if isinstance(infile, (str, unicode)):
        infile = open(infile, 'rb')
    dtype = type2dtype(typecode, type, dtype, True)
    if shape is None:
        shape = (-1,)
    if not isinstance(shape, tuple):
        shape = (shape,)
    if (list(shape).count(-1)>1):
        raise ValueError("At most one unspecified dimension in shape")
    if -1 not in shape:
        if sizing != STRICT:
            raise ValueError("sizing must be STRICT if size complete")
        arr = np.empty(shape, dtype)
        bytesleft=arr.nbytes
        bytesread=0
        while(bytesleft > _BLOCKSIZE):
            data = infile.read(_BLOCKSIZE)
            if len(data) != _BLOCKSIZE:
                raise EarlyEOFError("Unexpected EOF reading data for size complete array")
            arr.data[bytesread:bytesread+_BLOCKSIZE]=data
            bytesread += _BLOCKSIZE
            bytesleft -= _BLOCKSIZE
        if bytesleft > 0:
            data = infile.read(bytesleft)
            if len(data) != bytesleft:
                raise EarlyEOFError("Unexpected EOF reading data for size complete array")
            arr.data[bytesread:bytesread+bytesleft]=data
        return arr
    ##shape is incompletely specified
    ##read until EOF
    ##implementation 1: naively use memory blocks
    ##problematic because memory allocation can be double what is
    ##necessary (!)
    ##the most common case, namely reading in data from an unchanging
    ##file whose size may be determined before allocation, should be
    ##quick -- only one allocation will be needed.
    recsize = dtype.itemsize * np.product([i for i in shape if i != -1])
    blocksize = max(_BLOCKSIZE/recsize, 1)*recsize
    ##try to estimate file size
    try:
        curpos=infile.tell()
        infile.seek(0,2)
        endpos=infile.tell()
        infile.seek(curpos)
    except (AttributeError, IOError):
        initsize=blocksize
    else:
        initsize=max(1,(endpos-curpos)/recsize)*recsize
    buf = np.newbuffer(initsize)
    bytesread=0
    while 1:
        data=infile.read(blocksize)
        if len(data) != blocksize: ##eof
            break
        ##do we have space?
        if len(buf) < bytesread+blocksize:
            buf=_resizebuf(buf,len(buf)+blocksize)
            ## or rather a=resizebuf(a,2*len(a)) ?
        assert len(buf) >= bytesread+blocksize
        buf[bytesread:bytesread+blocksize]=data
        bytesread += blocksize
    if len(data) % recsize != 0:
        if sizing == STRICT:
            raise SizeMismatchError("Filesize does not match specified shape")
        if sizing == WARN:
            _warnings.warn("Filesize does not match specified shape",
                           SizeMismatchWarning)
        try:
            infile.seek(-(len(data) % recsize),1)
        except AttributeError:
            _warnings.warn("Could not rewind (no seek support)",
                           FileSeekWarning)
        except IOError:
            _warnings.warn("Could not rewind (IOError in seek)",
                           FileSeekWarning)
    datasize = (len(data)/recsize) * recsize
    if len(buf) != bytesread+datasize:
        buf=_resizebuf(buf,bytesread+datasize)
    buf[bytesread:bytesread+datasize]=data[:datasize]
    ##deduce shape from len(buf)
    shape = list(shape)
    uidx = shape.index(-1)
    shape[uidx]=len(buf) / recsize
    a = np.ndarray(shape=shape, dtype=type, buffer=buf)
    if a.dtype.char == '?':
        np.not_equal(a, 0, a)
    return a
