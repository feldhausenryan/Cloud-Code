#------------------------------------------------------------------------------
# Identifier
#------------------------------------------------------------------------------
def p_identifier(p):
    ''' identifier : NAME COLON NAME NEWLINE '''
    lhs = p[1]
    if lhs != 'id':
        msg = "'id' required. Got '%s' instead." % lhs
        syntax_error(msg, FakeToken(p.lexer.lexer, p.lineno(1)))
    p[0] = p[3]
