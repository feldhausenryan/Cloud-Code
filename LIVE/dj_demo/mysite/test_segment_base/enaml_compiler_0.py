#------------------------------------------------------------------------------
# Expression Compilers
#------------------------------------------------------------------------------
def replace_global_loads(codelist, explicit=None):
    """ A code transformer which rewrites LOAD_GLOBAL opcodes.
    This transform will replace the LOAD_GLOBAL opcodes with LOAD_NAME
    opcodes. The operation is performed in-place.
    Parameters
    ----------
    codelist : list
        The list of byteplay code ops to modify.
    explicit : set or None
        The set of global names declared explicitly and which should
        remain untransformed.
    """
    # Replacing LOAD_GLOBAL with LOAD_NAME enables dynamic scoping by
    # way of a custom locals mapping. The `call_func` function in the
    # `funchelper` module enables passing a locals map to a function.
    explicit = explicit or set()
    for idx, (op, op_arg) in enumerate(codelist):
        if op == LOAD_GLOBAL and op_arg not in explicit:
            codelist[idx] = (LOAD_NAME, op_arg)
