# line 7
def replace(func):
    def insteadfunc():
        print 'hello'
    return insteadfunc
