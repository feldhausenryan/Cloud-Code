# helper functions for creating __magic__ methods
def ophelper(f):
    def func(*args):
        args = list(args)
        for i, x in enumerate(args):
            if isConstant(x):
                args[i] = x = ConstantNode(x)
            if not isinstance(x, ExpressionNode):
                raise TypeError("unsupported object type: %s" % type(x))
        return f(*args)
    func.__name__ = f.__name__
    func.__doc__ = f.__doc__
    func.__dict__.update(f.__dict__)
    return func
