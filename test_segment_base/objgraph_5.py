# Print for each module the names of the other modules that use it.
#
def printcaller():
    files = file2def.keys()
    files.sort()
    for filename in files:
        callers = []
        for label in file2def[filename]:
            if undef2file.has_key(label):
                callers = callers + undef2file[label]
        if callers:
            callers.sort()
            print filename + ':'
            lastfn = ''
            for fn in callers:
                if fn <> lastfn:
                    print '\t' + fn
                lastfn = fn
        else:
            print filename + ': unused'
