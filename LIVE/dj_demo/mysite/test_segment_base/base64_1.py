# Useable as a script...
def test():
    """Small test program"""
    import sys, getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'deut')
    except getopt.error, msg:
        sys.stdout = sys.stderr
        print msg
        print """usage: %s [-d|-e|-u|-t] [file|-]
        -d, -u: decode
        -e: encode (default)
        -t: encode and decode string 'Aladdin:open sesame'"""%sys.argv[0]
        sys.exit(2)
    func = encode
    for o, a in opts:
        if o == '-e': func = encode
        if o == '-d': func = decode
        if o == '-u': func = decode
        if o == '-t': test1(); return
    if args and args[0] != '-':
        with open(args[0], 'rb') as f:
            func(f, sys.stdout)
    else:
        func(sys.stdin, sys.stdout)
