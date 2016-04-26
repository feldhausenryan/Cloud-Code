# This function is the actual implementation of the -m switch and direct
# execution of zipfiles and directories and is deliberately kept private.
# This avoids a repeat of the situation where run_module() no longer met the
# needs of mainmodule.c, but couldn't be changed because it was public
def _run_module_as_main(mod_name, alter_argv=True):
    """Runs the designated module in the __main__ namespace
       Note that the executed module will have full access to the
       __main__ namespace. If this is not desirable, the run_module()
       function should be used to run the module code in a fresh namespace.
       At the very least, these variables in __main__ will be overwritten:
           __name__
           __file__
           __loader__
           __package__
    """
    try:
        if alter_argv or mod_name != "__main__": # i.e. -m switch
            mod_name, loader, code, fname = _get_module_details(mod_name)
        else:          # i.e. directory or zipfile execution
            mod_name, loader, code, fname = _get_main_module_details()
    except ImportError as exc:
        msg = "%s: %s" % (sys.executable, str(exc))
        sys.exit(msg)
    pkg_name = mod_name.rpartition('.')[0]
    main_globals = sys.modules["__main__"].__dict__
    if alter_argv:
        sys.argv[0] = fname
    return _run_code(code, main_globals, None,
                     "__main__", fname, loader, pkg_name)
