# open a wave-file
def read(file, mmap=False):
    """
    Return the sample rate (in samples/sec) and data from a WAV file
    Parameters
    ----------
    file : file
        Input wav file.
    mmap : bool, optional
        Whether to read data as memory mapped. (Default: False)
        .. versionadded:: 0.12.0
    Returns
    -------
    rate : int
        Sample rate of wav file
    data : numpy array
        Data read from wav file
    Notes
    -----
    * The file can be an open file or a filename.
    * The returned sample rate is a Python integer
    * The data is returned as a numpy array with a
      data-type determined from the file.
    """
    if hasattr(file,'read'):
        fid = file
    else:
        fid = open(file, 'rb')
    fsize = _read_riff_chunk(fid)
    noc = 1
    bits = 8
    while (fid.tell() < fsize):
        # read the next chunk
        chunk_id = fid.read(4)
        if chunk_id == b'fmt ':
            size, comp, noc, rate, sbytes, ba, bits = _read_fmt_chunk(fid)
        elif chunk_id == b'data':
            data = _read_data_chunk(fid, noc, bits, mmap=mmap)
        elif chunk_id == b'LIST':
            # Someday this could be handled properly but for now skip it
            _skip_unknown_chunk(fid)
        else:
            warnings.warn("Chunk (non-data) not understood, skipping it.",
                          WavFileWarning)
            _skip_unknown_chunk(fid)
    fid.close()
    return rate, data
