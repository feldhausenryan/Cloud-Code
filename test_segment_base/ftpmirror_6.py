# Write a dictionary to a file in a way that can be read back using
# rval() but is still somewhat readable (i.e. not a single long line).
# Also creates a backup file.
def writedict(dict, filename):
    dir, fname = os.path.split(filename)
    tempname = os.path.join(dir, '@' + fname)
    backup = os.path.join(dir, fname + '~')
    try:
        os.unlink(backup)
    except os.error:
        pass
    fp = open(tempname, 'w')
    fp.write('{\n')
    for key, value in dict.items():
        fp.write('%r: %r,\n' % (key, value))
    fp.write('}\n')
    fp.close()
    try:
        os.rename(filename, backup)
    except os.error:
        pass
    os.rename(tempname, filename)
