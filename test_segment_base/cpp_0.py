# Whitespace
def t_CPP_WS(t):
    r'\s+'
    t.lexer.lineno += t.value.count("\n")
    return t
