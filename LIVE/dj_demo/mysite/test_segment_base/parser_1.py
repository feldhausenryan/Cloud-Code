#------------------------------------------------------------------------------
# Declaration
#------------------------------------------------------------------------------
def p_declaration1(p):
    ''' declaration : ENAMLDEF NAME LPAR NAME RPAR COLON declaration_body '''
    doc, idn, items = p[7]
    p[0] = enaml_ast.Declaration(p[2], p[4], idn, doc, items, p.lineno(1))
