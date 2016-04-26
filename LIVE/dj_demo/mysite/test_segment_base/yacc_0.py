# Python 2.x/3.0 compatibility.
def load_ply_lex():
    if sys.version_info[0] < 3:
        import lex
    else:
        import ply.lex as lex
    return lex
