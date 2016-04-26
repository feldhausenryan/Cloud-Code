# Print undefined names and where they are used.
#
def printundef():
    undefs = {}
    for filename in file2undef.keys():
        for ext in file2undef[filename]:
            if not def2file.has_key(ext):
                store(undefs, ext, filename)
    elist = undefs.keys()
    elist.sort()
    for ext in elist:
        print ext + ':'
        flist = undefs[ext]
        flist.sort()
        for filename in flist:
            print '\t' + filename
