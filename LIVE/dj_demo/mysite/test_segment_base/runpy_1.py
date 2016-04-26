# Helper to get the loader, code and filename for a module
def _get_module_details(mod_name):
    loader = get_loader(mod_name)
    if loader is None:
        raise ImportError("No module named %s" % mod_name)
    if loader.is_package(mod_name):
        if mod_name == "__main__" or mod_name.endswith(".__main__"):
            raise ImportError("Cannot use package as __main__ module")
        try:
            pkg_main_name = mod_name + ".__main__"
            return _get_module_details(pkg_main_name)
        except ImportError, e:
            raise ImportError(("%s; %r is a package and cannot " +
                               "be directly executed") %(e, mod_name))
    code = loader.get_code(mod_name)
    if code is None:
        raise ImportError("No code object available for %s" % mod_name)
    filename = _get_filename(loader, mod_name)
    return mod_name, loader, code, filename
