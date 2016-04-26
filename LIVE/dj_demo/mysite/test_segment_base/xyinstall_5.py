# Main ------
def main(file, argv, scripts=[], prefs_filename='', prefs=(), other=[]):
    if len(argv) > 1:
        if argv[1] == '-install':
            install(file, scriptlist=scripts, other=other)
        elif argv[1] == '-remove':
            remove(file, scriptlist=scripts, other=other)
        else:
            print "Script was called with option %s" % sys.argv[1]
    else:
        print "Module <xyinstall.main>: options -install or -remove"
        print "(xyinstall %s)" % __version__
