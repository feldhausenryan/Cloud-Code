# Main program
#
def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: pdeps file.py file.py ...'
        return 2
    #
    table = {}
    for arg in args:
        process(arg, table)
    #
    print '--- Uses ---'
    printresults(table)
    #
    print '--- Used By ---'
    inv = inverse(table)
    printresults(inv)
    #
    print '--- Closure of Uses ---'
    reach = closure(table)
    printresults(reach)
    #
    print '--- Closure of Used By ---'
    invreach = inverse(reach)
    printresults(invreach)
    #
    return 0
