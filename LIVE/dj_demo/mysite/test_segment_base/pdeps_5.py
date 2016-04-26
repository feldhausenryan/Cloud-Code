# Tabulate results neatly
#
def printresults(table):
    modules = table.keys()
    maxlen = 0
    for mod in modules: maxlen = max(maxlen, len(mod))
    modules.sort()
    for mod in modules:
        list = table[mod]
        list.sort()
        print mod.ljust(maxlen), ':',
        if mod in list:
            print '(*)',
        for ref in list:
            print ref,
        print
