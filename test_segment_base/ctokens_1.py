# Comment (C++-Style)
def t_CPPCOMMENT(t):
    r'//.*\n'
    t.lexer.lineno += 1
    return t
