# Demonstration and testing.
#
def demo():
    import sys
    import getopt
    options, args = getopt.getopt(sys.argv[1:], 'r')
    if len(args) != 2:
        raise getopt.GetoptError('need exactly two args', None)
    dd = dircmp(args[0], args[1])
    if ('-r', '') in options:
        dd.report_full_closure()
    else:
        dd.report()
