# Print warning messages about names defined in more than one file.
#
def warndups():
    savestdout = sys.stdout
    sys.stdout = sys.stderr
    names = def2file.keys()
    names.sort()
    for name in names:
        if len(def2file[name]) > 1:
            print 'warning:', name, 'multiply defined:',
            print flat(def2file[name])
    sys.stdout = savestdout
