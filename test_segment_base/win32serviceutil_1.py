# Utility functions for Services, to allow persistant properties.
def SetServiceCustomOption(serviceName, option, value):
    try:
        serviceName = serviceName._svc_name_
    except AttributeError:
        pass
    key = win32api.RegCreateKey(win32con.HKEY_LOCAL_MACHINE, "System\\CurrentControlSet\\Services\\%s\\Parameters" % serviceName)
    try:
        if type(value)==type(0):
            win32api.RegSetValueEx(key, option, 0, win32con.REG_DWORD, value);
        else:
            win32api.RegSetValueEx(key, option, 0, win32con.REG_SZ, value);
    finally:
        win32api.RegCloseKey(key)
