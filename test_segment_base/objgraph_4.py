# Print all names that were undefined in some module and where they are
# defined.
#
def printcallee():
    flist = file2undef.keys()
    flist.sort()
    for filename in flist:
        print filename + ':'
        elist = file2undef[filename]
        elist.sort()
        for ext in elist:
            if len(ext) >= 8:
                tabs = '\t'
            else:
                tabs = '\t\t'
            if not def2file.has_key(ext):
                print '\t' + ext + tabs + ' *undefined'
            else:
                print '\t' + ext + tabs + flat(def2file[ext])
