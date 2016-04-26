# fixme: This is the same code as in the Envisage import manager but we don't
# want naming to be dependent on Envisage, so we need some other package
# for useful 'Python' tools etc.
def _import_symbol(symbol_path):
    """ Imports the symbol defined by 'symbol_path'.
    'symbol_path' is a string in the form 'foo.bar.baz' which is turned
    into an import statement 'from foo.bar import baz' (ie. the last
    component of the name is the symbol name, the rest is the package/
    module path to load it from).
    """
    components = symbol_path.split('.')
    module_name = '.'.join(components[:-1])
    symbol_name = components[-1]
    module = __import__(module_name, globals(), locals(), [symbol_name])
    symbol = getattr(module, symbol_name)
    return symbol
