#------------------------------------------------------------------------------
# Instantiation
#------------------------------------------------------------------------------
def p_instantiation1(p):
    ''' instantiation : NAME COLON instantiation_body '''
    identifier, items = p[3]
    p[0] = enaml_ast.Instantiation(p[1], identifier, items, p.lineno(1))
