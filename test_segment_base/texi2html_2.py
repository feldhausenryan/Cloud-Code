# Convert a node name into a file name
def makefile(nodename):
    nodename = nodename.strip()
    return fixfunnychars(nodename) + '.html'
