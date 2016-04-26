# Helper to remove a file or directory tree
def remove(fullname):
    if os.path.isdir(fullname) and not os.path.islink(fullname):
        try:
            names = os.listdir(fullname)
        except os.error:
            names = []
        ok = 1
        for name in names:
            if not remove(os.path.join(fullname, name)):
                ok = 0
        if not ok:
            return 0
        try:
            os.rmdir(fullname)
        except os.error, msg:
            print "Can't remove local directory %r: %s" % (fullname, msg)
            return 0
    else:
        try:
            os.unlink(fullname)
        except os.error, msg:
            print "Can't remove local file %r: %s" % (fullname, msg)
            return 0
    return 1
