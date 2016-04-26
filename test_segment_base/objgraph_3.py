# Read one input file and merge the data into the tables.
# Argument is an open file.
#
def readinput(fp):
    while 1:
        s = fp.readline()
        if not s:
            break
        # If you get any output from this line,
        # it is probably caused by an unexpected input line:
        if matcher.search(s) < 0: s; continue # Shouldn't happen
        (ra, rb), (r1a, r1b), (r2a, r2b), (r3a, r3b) = matcher.regs[:4]
        fn, name, type = s[r1a:r1b], s[r3a:r3b], s[r2a:r2b]
        if type in definitions:
            store(def2file, name, fn)
            store(file2def, fn, name)
        elif type in externals:
            store(file2undef, fn, name)
            store(undef2file, name, fn)
        elif not type in ignore:
            print fn + ':' + name + ': unknown type ' + type
