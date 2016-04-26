##################################################################
#                         FUNCTION LIST                          #
##################################################################
def listing(f):
    "Pretty print the internals of your function"
    assert_(inspect.isfunction(f))
    filename = f.func_code.co_filename
    try:
        lines = open(filename).readlines()
    except:
        lines = None
    pc = 0
    s = ''
    lastLine = None
    for op,arg,name in opcodize(f.func_code.co_code):
        if lines and name == 'SET_LINENO':
            source = lines[arg-1][:-1]
            while lastLine and lastLine < arg-1:
                nonEmittingSource = lines[lastLine][:-1]
                lastLine += 1
                s += '%3s  %20s %5s : %s\n'%(
                    '','','',nonEmittingSource)
            lastLine = arg
        else:
            source = ''
        if arg is None: arg = ''
        s += '%3d] %20s %5s : %s\n'%(pc,name,arg,source)
        if op >= haveArgument:
            pc += 3
        else:
            pc += 1
    return s
