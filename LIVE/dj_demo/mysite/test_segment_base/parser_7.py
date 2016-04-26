# This keyword argument needs to be asserted as a NAME, but using NAME
# here causes ambiguity in the parse tables.
def p_argument3(p):
    ''' argument : test EQUAL test '''
    arg = p[1]
    assert isinstance(arg, ast.Name), 'Keyword arg must be a Name.'
    value = p[3]
    p[0] = ast.keyword(arg=arg.id, value=value)
