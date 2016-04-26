#------------------------------------------------------------------------------
# Attribute Declaration
#------------------------------------------------------------------------------
def p_attribute_declaration1(p):
    ''' attribute_declaration : NAME NAME NEWLINE '''
    p[0] = build_attr_declaration(p[1], p[2], None, None, p.lineno(1), p)
