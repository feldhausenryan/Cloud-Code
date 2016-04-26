#------------------------------------------------------------------------------
# Enaml Module
#------------------------------------------------------------------------------
# These special rules to handle the variations of newline and endmarkers
# are because of the various lexer states that deal with python blocks
# and enaml code, as well as completely empty files.
def p_enaml1(p):
    ''' enaml : enaml_module NEWLINE ENDMARKER
              | enaml_module ENDMARKER '''
    p[0] = p[1]
