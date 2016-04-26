# TODO: Replace this with fileobj_mode
def _get_file_mode(filename, default='copyonwrite'):
    """
    Allow file object to already be opened in any of the valid modes and
    and leave the file in the same state (opened or closed) as when
    the function was called.
    """
    mode = default
    closed = True
    if hasattr(filename, 'closed'):
        closed = filename.closed
    elif hasattr(filename, 'fileobj') and filename.fileobj is not None:
        closed = filename.fileobj.closed
    if (isfile(filename) or
        isinstance(filename, gzip.GzipFile) and not closed):
        if isinstance(filename, gzip.GzipFile):
            file_mode = filename.fileobj.mode
        else:
            file_mode = filename.mode
        for key, val in PYTHON_MODES.iteritems():
            if val == file_mode:
                mode = key
                break
    return mode, closed
