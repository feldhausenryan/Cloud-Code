# [XX] Normalize with respect to os.path.pardir?
def _module_relative_path(module, path):
    if not inspect.ismodule(module):
        raise TypeError, 'Expected a module: %r' % module
    if path.startswith('/'):
        raise ValueError, 'Module-relative files may not have absolute paths'
    # Find the base directory for the path.
    if hasattr(module, '__file__'):
        # A normal module/package
        basedir = os.path.split(module.__file__)[0]
    elif module.__name__ == '__main__':
        # An interactive session.
        if len(sys.argv)>0 and sys.argv[0] != '':
            basedir = os.path.split(sys.argv[0])[0]
        else:
            basedir = os.curdir
    else:
        # A module w/o __file__ (this includes builtins)
        raise ValueError("Can't resolve paths relative to the module " +
                         module + " (it has no __file__)")
    # Combine the base directory and the path.
    return os.path.join(basedir, *(path.split('/')))
