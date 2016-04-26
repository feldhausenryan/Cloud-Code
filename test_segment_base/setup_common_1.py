"""

def pyod(filename):
    """Python implementation of the od UNIX utility (od -b, more exactly).

    Parameters
    ----------
    filename: str
        name of the file to get the dump from.

    Returns
    -------
    out: seq
        list of lines of od output
    Note
    ----
    We only implement enough to get the necessary information for long double
    representation, this is not intended as a compatible replacement for od.
    """
    def _pyod2():
        out = []
        fid = open(filename, 'rb')
        try:
            yo = [int(oct(int(binascii.b2a_hex(o), 16))) for o in fid.read()]
            for i in range(0, len(yo), 16):
                line = ['%07d' % int(oct(i))]
                line.extend(['%03d' % c for c in yo[i:i+16]])
                out.append(" ".join(line))
            return out
        finally:
            fid.close()
