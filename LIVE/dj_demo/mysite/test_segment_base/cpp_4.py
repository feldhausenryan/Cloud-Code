# Comment
def t_CPP_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*?\n)'
    t.lexer.lineno += t.value.count("\n")
    return t
