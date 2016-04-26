# We need to import win32api to determine the Windows system directory,
# so we can copy our system files there - but importing win32api will
# load the pywintypes.dll already in the system directory preventing us
# from updating them!
# So, we pull the same trick pywintypes.py does, but it loads from
# our pywintypes_system32 directory.
def LoadSystemModule(lib_dir, modname):
    # See if this is a debug build.
    import imp
    for suffix_item in imp.get_suffixes():
        if suffix_item[0]=='_d.pyd':
            suffix = '_d'
            break
    else:
        suffix = ""
    filename = "%s%d%d%s.dll" % \
               (modname, sys.version_info[0], sys.version_info[1], suffix)
    filename = os.path.join(lib_dir, "pywin32_system32", filename)
    mod = imp.load_dynamic(modname, filename)
