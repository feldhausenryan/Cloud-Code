# Character constant 'c' or L'c'
def t_CPP_CHAR(t):
    r'(L)?\'([^\\\n]|(\\(.|\n)))*?\''
    t.lexer.lineno += t.value.count("\n")
    return t
