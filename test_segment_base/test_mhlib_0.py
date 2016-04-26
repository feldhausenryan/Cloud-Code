# These next 2 functions are copied from test_glob.py.
def mkdirs(fname):
    if os.path.exists(fname) or fname == '':
        return
    base, file = os.path.split(fname)
    mkdirs(base)
    os.mkdir(fname)
