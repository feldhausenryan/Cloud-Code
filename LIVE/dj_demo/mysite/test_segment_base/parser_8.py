# The varargslist_list handlers return a 2-tuple of (args, defaults) lists
def p_varargslist_list1(p):
    ''' varargslist_list : COMMA fpdef '''
    p[0] = ([p[2]], [])
