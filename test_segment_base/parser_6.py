#------------------------------------------------------------------------------
# Python Grammar
#------------------------------------------------------------------------------
def p_suite1(p):
    ''' suite : simple_stmt '''
    # stmt may be a list of simple_stmt due to this piece of grammar:
    # simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
    stmt = p[1]
    if isinstance(stmt, list):
        res = stmt
    else:
        res = [stmt]
    p[0] = res
