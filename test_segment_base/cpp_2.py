# String literal
def t_CPP_STRING(t):
    r'\"([^\\\n]|(\\(.|\n)))*?\"'
    t.lexer.lineno += t.value.count("\n")
    return t
