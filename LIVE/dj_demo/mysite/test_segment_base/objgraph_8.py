# Main program
#
def main():
    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'cdu')
    except getopt.error:
        sys.stdout = sys.stderr
        print 'Usage:', os.path.basename(sys.argv[0]),
        print           '[-cdu] [file] ...'
        print '-c: print callers per objectfile'
        print '-d: print callees per objectfile'
        print '-u: print usage of undefined symbols'
        print 'If none of -cdu is specified, all are assumed.'
        print 'Use "nm -o" to generate the input (on IRIX: "nm -Bo"),'
        print 'e.g.: nm -o /lib/libc.a | objgraph'
        return 1
    optu = optc = optd = 0
    for opt, void in optlist:
        if opt == '-u':
            optu = 1
        elif opt == '-c':
            optc = 1
        elif opt == '-d':
            optd = 1
    if optu == optc == optd == 0:
        optu = optc = optd = 1
    if not args:
        args = ['-']
    for filename in args:
        if filename == '-':
            readinput(sys.stdin)
        else:
            readinput(open(filename, 'r'))
    #
    warndups()
    #
    more = (optu + optc + optd > 1)
    if optd:
        if more:
            print '---------------All callees------------------'
        printcallee()
    if optu:
        if more:
            print '---------------Undefined callees------------'
        printundef()
    if optc:
        if more:
            print '---------------All Callers------------------'
        printcaller()
    return 0
