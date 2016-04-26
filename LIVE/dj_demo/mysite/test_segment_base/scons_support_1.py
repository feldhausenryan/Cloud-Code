#-------------------------
# From template generators
#-------------------------
# XXX: this is general and can be used outside numpy.core.
def do_generate_from_template(targetfile, sourcefile, env):
    t = open(targetfile, 'w')
    s = open(sourcefile, 'r')
    allstr = s.read()
    s.close()
    writestr = process_str(allstr)
    t.write(writestr)
    t.close()
    return 0
