# Patch up any missing module names in the params, replacing them with
# the DLL name that hosts this extension/filter.
def _PatchParamsModule(params, dll_name, file_must_exist = True):
    if file_must_exist:
        if not os.path.isfile(dll_name):
            raise ConfigurationError("%s does not exist" % (dll_name,))
    # Patch up all references to the DLL.
    for f in params.Filters:
        if f.Path is None: f.Path = dll_name
    for d in params.VirtualDirs:
        for sm in d.ScriptMaps:
            if sm.Module is None: sm.Module = dll_name
