# Print usage message and exit
def usage(*args):
    sys.stdout = sys.stderr
    for msg in args: print msg
    print __doc__
    sys.exit(2)
