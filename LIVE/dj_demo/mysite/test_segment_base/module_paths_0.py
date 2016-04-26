#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------
def find_module(name, path=None):
    """imp.find_module variant that only return path of module.
    The `imp.find_module` returns a filehandle that we are not interested in.
    Also we ignore any bytecode files that `imp.find_module` finds.
    Parameters
    ----------
    name : str
        name of module to locate
    path : list of str
        list of paths to search for `name`. If path=None then search sys.path
    Returns
    -------
    filename : str
        Return full path of module or None if module is missing or does not have
        .py or .pyw extension
    """
    if name is None:
        return None
    try:
        file, filename, _ = imp.find_module(name, path)
    except ImportError:
        return None
    if file is None:
        return filename
    else:
        file.close()
    if os.path.splitext(filename)[1] in [".py", "pyc"]:
        return filename
    else:
        return None
