# Less conservative replacement for sys.getdefaultencoding, that will try
# to match the environment.
# Defined here as central function, so if we find better choices, we
# won't need to make changes all over IPython.
def getdefaultencoding():
    """Return IPython's guess for the default encoding for bytes as text.
    Asks for stdin.encoding first, to match the calling Terminal, but that
    is often None for subprocesses.  Fall back on locale.getpreferredencoding()
    which should be a sensible platform default (that respects LANG environment),
    and finally to sys.getdefaultencoding() which is the most conservative option,
    and usually ASCII.
    """
    enc = get_stream_enc(sys.stdin)
    if not enc or enc=='ascii':
        try:
            # There are reports of getpreferredencoding raising errors
            # in some cases, which may well be fixed, but let's be conservative here.
            enc = locale.getpreferredencoding()
        except Exception:
            pass
    return enc or sys.getdefaultencoding()
