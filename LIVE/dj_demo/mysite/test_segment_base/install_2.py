# We support 2 ways of extending our command-line/install support.
# * Many of the installation items allow you to specify "PreInstall",
#   "PostInstall", "PreRemove" and "PostRemove" hooks
#   All hooks are called with the 'params' object being operated on, and
#   the 'optparser' options for this session (ie, the command-line options)
#   PostInstall for VirtualDirectories and Filters both have an additional
#   param - the ADSI object just created.
# * You can pass your own option parser for us to use, and/or define a map
#   with your own custom arg handlers.  It is a map of 'arg'->function.
#   The function is called with (options, log_fn, arg).  The function's
#   docstring is used in the usage output.
def HandleCommandLine(params, argv=None, conf_module_name = None,
                      default_arg = "install",
                      opt_parser = None, custom_arg_handlers = {}):
    """Perform installation or removal of an ISAPI filter or extension.
    This module handles standard command-line options and configuration
    information, and installs, removes or updates the configuration of an
    ISAPI filter or extension.
    You must pass your configuration information in params - all other
    arguments are optional, and allow you to configure the installation
    process.
    """
    global verbose
    from optparse import OptionParser
    argv = argv or sys.argv
    if not conf_module_name:
        conf_module_name = sys.argv[0]
        # convert to a long name so that if we were somehow registered with
        # the "short" version but unregistered with the "long" version we
        # still work (that will depend on exactly how the installer was
        # started)
        try:
            conf_module_name = win32api.GetLongPathName(conf_module_name)
        except win32api.error, exc:
            log(2, "Couldn't determine the long name for %r: %s" %
                (conf_module_name, exc))
    if opt_parser is None:
        # Build our own parser.
        parser = OptionParser(usage='')
    else:
        # The caller is providing their own filter, presumably with their
        # own options all setup.
        parser = opt_parser
    # build a usage string if we don't have one.
    if not parser.get_usage():
        all_handlers = standard_arguments.copy()
        all_handlers.update(custom_arg_handlers)
        parser.set_usage(build_usage(all_handlers))
    # allow the user to use uninstall as a synonym for remove if it wasn't
    #  defined by the custom arg handlers.
    all_handlers.setdefault('uninstall', all_handlers['remove'])
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print status messages to stdout")
    parser.add_option("-v", "--verbosity", action="count",
                      dest="verbose", default=1,
                      help="increase the verbosity of status messages")
    parser.add_option("", "--server", action="store",
                      help="Specifies the IIS server to install/uninstall on." \
                           " Default is '%s/1'" % (_IIS_OBJECT,))
    (options, args) = parser.parse_args(argv[1:])
    MergeStandardOptions(options, params)
    verbose = options.verbose
    if not args:
        args = [default_arg]
    try:
        for arg in args:
            handler = all_handlers[arg]
            handler(conf_module_name, params, options, log)
    except (ItemNotFound, InstallationError), details:
        if options.verbose > 1:
            traceback.print_exc()
        print "%s: %s" % (details.__class__.__name__, details)
    except KeyError:
        parser.error("Invalid arg '%s'" % arg)
