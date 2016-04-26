# N.B. This function is a monkeypatch we are currently not applying.
# It was written some time ago, to fix an apparent Python bug with
# codeobj.co_firstlineno . Unfortunately, we don't know under what conditions
# the bug occurred, so we can't tell if it has been fixed. If it reappears, we
# will apply the monkeypatch again. Also, note that findsource() is not called
# by our code at this time - we don't know if it was when the monkeypatch was
# written, or if the monkeypatch is needed for some other code (like a debugger).
# For the discussion about not applying it, see gh-1229. TK, Jan 2011.
def findsource(object):
    """Return the entire source file and starting line number for an object.
    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a list of all the lines
    in the file and the line number indexes a line in that list.  An IOError
    is raised if the source code cannot be retrieved.
    FIXED version with which we monkeypatch the stdlib to work around a bug."""
    file = getsourcefile(object) or getfile(object)
    # If the object is a frame, then trying to get the globals dict from its
    # module won't work. Instead, the frame object itself has the globals
    # dictionary.
    globals_dict = None
    if inspect.isframe(object):
        # XXX: can this ever be false?
        globals_dict = object.f_globals
    else:
        module = getmodule(object, file)
        if module:
            globals_dict = module.__dict__
    lines = linecache.getlines(file, globals_dict)
    if not lines:
        raise IOError('could not get source code')
    if ismodule(object):
        return lines, 0
    if isclass(object):
        name = object.__name__
        pat = re.compile(r'^(\s*)class\s*' + name + r'\b')
        # make some effort to find the best matching class definition:
        # use the one with the least indentation, which is the one
        # that's most probably not inside a function definition.
        candidates = []
        for i in range(len(lines)):
            match = pat.match(lines[i])
            if match:
                # if it's at toplevel, it's already the best one
                if lines[i][0] == 'c':
                    return lines, i
                # else add whitespace to candidate list
                candidates.append((match.group(1), i))
        if candidates:
            # this will sort by whitespace, and by line number,
            # less whitespace first
            candidates.sort()
            return lines, candidates[0][1]
        else:
            raise IOError('could not find class definition')
    if ismethod(object):
        object = object.im_func
    if isfunction(object):
        object = object.func_code
    if istraceback(object):
        object = object.tb_frame
    if isframe(object):
        object = object.f_code
    if iscode(object):
        if not hasattr(object, 'co_firstlineno'):
            raise IOError('could not find function definition')
        pat = re.compile(r'^(\s*def\s)|(.*(?<!\w)lambda(:|\s))|^(\s*@)')
        pmatch = pat.match
        # fperez - fix: sometimes, co_firstlineno can give a number larger than
        # the length of lines, which causes an error.  Safeguard against that.
        lnum = min(object.co_firstlineno,len(lines))-1
        while lnum > 0:
            if pmatch(lines[lnum]): break
            lnum -= 1
        return lines, lnum
    raise IOError('could not find code object')
