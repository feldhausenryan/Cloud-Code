# Get the system directory, which may be the Wow64 directory if we are a 32bit
# python on a 64bit OS.
def get_system_dir():
    import win32api # we assume this exists.
    try:
        import pythoncom
        import win32process
        from win32com.shell import shell, shellcon
        try:
            if win32process.IsWow64Process():
                return shell.SHGetSpecialFolderPath(0,shellcon.CSIDL_SYSTEMX86)
            return shell.SHGetSpecialFolderPath(0,shellcon.CSIDL_SYSTEM)
        except (pythoncom.com_error, win32process.error):
            return win32api.GetSystemDirectory()
    except ImportError:
        return win32api.GetSystemDirectory()
