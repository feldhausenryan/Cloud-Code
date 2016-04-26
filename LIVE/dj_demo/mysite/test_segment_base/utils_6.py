#==============================================================================
# Module, scripts, programs
#==============================================================================
def get_module_path(modname):
    """Return module *modname* base path"""
    module = sys.modules.get(modname, __import__(modname))
    return osp.abspath(osp.dirname(module.__file__))
