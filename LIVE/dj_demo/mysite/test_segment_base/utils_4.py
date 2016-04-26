#==============================================================================
# Interface checking
#==============================================================================
def assert_interface_supported(klass, iface):
    """Makes sure a class supports an interface"""
    for name, func in list(iface.__dict__.items()):
        if name == '__inherits__':
            continue
        if isinstance(func, collections.Callable):
            assert hasattr(klass, name), \
                   "Attribute %s missing from %r" % (name, klass)
            imp_func = getattr(klass, name)
            imp_code = get_func_code(imp_func)
            code = get_func_code(func)
            imp_nargs = imp_code.co_argcount
            nargs = code.co_argcount
            if imp_code.co_varnames[:imp_nargs] != code.co_varnames[:nargs]:
                assert False, "Arguments of %s.%s differ from interface: "\
                              "%r!=%r" % (
                                klass.__name__, get_func_name(imp_func),
                                imp_code.co_varnames[:imp_nargs],
                                code.co_varnames[:nargs]
                                )
        else:
            pass  # should check class attributes for consistency
