# The callback made when IIS completes the asynch write.
def io_callback(ecb, fp, cbIO, errcode):
    print "IO callback", ecb, fp, cbIO, errcode
    chunk = fp.read(CHUNK_SIZE)
    if chunk:
        ecb.WriteClient(chunk, isapicon.HSE_IO_ASYNC)
        # and wait for the next callback to say this chunk is done.
    else:
        # eof - say we are complete.
        fp.close()
        ecb.DoneWithSession()
