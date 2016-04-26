#------------------------------------------------------------------------------
#  Copyright (c) 2013, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
def _format_source_error(filename, lineno, block):
    """ A helper function which generates an error string.
    This function handles the work of reading the lines of the file
    which bracket the error, and formatting a string which points to
    the offending line. The output is similar to:
    File "foo.py", line 42, in bar()
           41 def bar():
    ---->  42     a = a + 1
           43     return a
    Parameters
    ----------
    filename : str
        The full path to the offending file.
    lineno : int
        The line number of the offending like.
    block : str
        The name of the block scope in which the error occured. In the
        sample above, the block scope is 'bar'.
    Returns
    -------
    result : str
        A nicely formatted string for including in an exception. If the
        file cannot be opened, the source lines will note be included.
    """
    text = 'File "%s", line %d, in %s()' % (filename, lineno, block)
    start_lineno = max(0, lineno - 1)
    end_lineno = start_lineno + 2
    lines = []
    try:
        with open(filename, 'r') as f:
            for idx, line in enumerate(f, 1):
                if idx >= start_lineno and idx <= end_lineno:
                    lines.append((idx, line))
                elif idx > end_lineno:
                    break
    except IOError:
        pass
    if len(lines) > 0:
        digits = str(len(str(end_lineno)))
        line_templ = '\n----> %' + digits + 'd %s'
        other_templ = '\n      %' + digits + 'd %s'
        for lno, line in lines:
            line = line.rstrip()
            if lno == lineno:
                text += line_templ % (lno, line)
            else:
                text += other_templ % (lno, line)
    return text
