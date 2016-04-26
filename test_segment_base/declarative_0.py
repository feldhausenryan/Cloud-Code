#------------------------------------------------------------------------------
# Declarative Helpers
#------------------------------------------------------------------------------
def _compute_default(obj, name):
    """ Compute the default value for an expression.
    This is a private function used by Declarative for allowing default
    values of attributes to be provided by bound expression objects
    without requiring an explicit initialization graph.
    """
    try:
        return obj.eval_expression(name)
    except DynamicAttributeError:
        raise  # Reraise a propagating initialization error.
    except Exception:
        import traceback
        # XXX I'd rather not hack into Declarative's private api.
        expr = obj._expressions[name]
        filename = expr._func.func_code.co_filename
        lineno = expr._func.func_code.co_firstlineno
        args = (filename, lineno, traceback.format_exc())
        msg = ('Error initializing expression (%r line %s). Orignal '
               'exception was:\n%s')
        raise DynamicAttributeError(msg % args)
