# FIXME: workaround for old splitlines()
def _join_lines(lines):
    """join lines that have been written by splitlines()
    Has logic to protect against `splitlines()`, which
    should have been `splitlines(True)`
    """
    if lines and lines[0].endswith(('\n', '\r')):
        # created by splitlines(True)
        return u''.join(lines)
    else:
        # created by splitlines()
        return u'\n'.join(lines)
