# register plugin
def DllRegisterServer():
    comclass = IEToolbar
    # register toolbar with IE
    try:
        print "Trying to register Toolbar.\n"
        hkey = _winreg.CreateKey( _winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Internet Explorer\\Toolbar" )
        subKey = _winreg.SetValueEx( hkey, comclass._reg_clsid_, 0, _winreg.REG_BINARY, "\0" )
    except WindowsError:
        print "Couldn't set registry value.\nhkey: %d\tCLSID: %s\n" % ( hkey, comclass._reg_clsid_ )
    else:
        print "Set registry value.\nhkey: %d\tCLSID: %s\n" % ( hkey, comclass._reg_clsid_ )
    # TODO: implement reg settings for standard toolbar button
