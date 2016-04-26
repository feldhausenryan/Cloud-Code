# A couple of utilities to ensure these tests work the same from a source or a
# binary install
def pyfile(fname):
    return os.path.normcase(re.sub('.py[co]$', '.py', fname))
