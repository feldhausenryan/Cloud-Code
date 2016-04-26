# XXX (ncoghlan): Perhaps expose the C API function
# as imp.get_importer instead of reimplementing it in Python?
def _get_importer(path_name):
    """Python version of PyImport_GetImporter C API function"""
    cache = sys.path_importer_cache
    try:
        importer = cache[path_name]
    except KeyError:
        # Not yet cached. Flag as using the
        # standard machinery until we finish
        # checking the hooks
        cache[path_name] = None
        for hook in sys.path_hooks:
            try:
                importer = hook(path_name)
                break
            except ImportError:
                pass
        else:
            # The following check looks a bit odd. The trick is that
            # NullImporter raises ImportError if the supplied path is a
            # *valid* directory entry (and hence able to be handled
            # by the standard import machinery)
            try:
                importer = imp.NullImporter(path_name)
            except ImportError:
                return None
        cache[path_name] = importer
    return importer
