# unregister plugin
def DllUnregisterServer():
    comclass = IEToolbar
    # unregister toolbar from internet explorer
    try:
        print "Trying to unregister Toolbar.\n"
        hkey = _winreg.CreateKey( _winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Internet Explorer\\Toolbar" )
        _winreg.DeleteValue( hkey, comclass._reg_clsid_ )
    except WindowsError:
        print "Couldn't delete registry value.\nhkey: %d\tCLSID: %s\n" % ( hkey, comclass._reg_clsid_ )
    else:
        print "Deleting reg key succeeded.\n"
