################################################################################
# Utility functions.
################################################################################
def import_symbol(symbol_path):
    """ Import the symbol defined by the specified symbol path.
    Copied from envisage's import manager.
    """
    if ':' in symbol_path:
        module_name, symbol_name = symbol_path.split(':')
        module = import_module(module_name)
        symbol = eval(symbol_name, module.__dict__)
    else:
        components = symbol_path.split('.')
        module_name = '.'.join(components[:-1])
        symbol_name = components[-1]
        module = __import__(
            module_name, globals(), locals(), [symbol_name]
        )
        symbol = getattr(module, symbol_name)
    return symbol
