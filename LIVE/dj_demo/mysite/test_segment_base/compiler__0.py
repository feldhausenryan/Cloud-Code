# (Copied from python2.4/compiler/transformer.py)
def parse(buf, mode="exec", transformer=None):
    'Extends compiler.parse to take a transformer.'
    if transformer is None:
        transformer = Transformer()
    if mode == "exec" or mode == "single":
        return transformer.parsesuite(buf)
    elif mode == "eval":
        return transformer.parseexpr(buf)
    else:
        raise ValueError("compile() arg 3 must be"
                         " 'exec' or 'eval' or 'single'")
