# There are others in sndhdr that don't have MIME types. :(
# Additional ones to be added to sndhdr? midi, mp3, realaudio, wma??
def _whatsnd(data):
    """Try to identify a sound file type.
    sndhdr.what() has a pretty cruddy interface, unfortunately.  This is why
    we re-do it here.  It would be easier to reverse engineer the Unix 'file'
    command and use the standard 'magic' file, as shipped with a modern Unix.
    """
    hdr = data[:512]
    fakefile = StringIO(hdr)
    for testfn in sndhdr.tests:
        res = testfn(hdr, fakefile)
        if res is not None:
            return _sndhdr_MIMEmap.get(res[0])
    return None
