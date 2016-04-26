#------------------------------------------------------------------------------
# Attribute Binding
#------------------------------------------------------------------------------
def p_attribute_binding(p):
    ''' attribute_binding : NAME binding '''
    p[0] = enaml_ast.AttributeBinding(p[1], p[2], p.lineno(1))
