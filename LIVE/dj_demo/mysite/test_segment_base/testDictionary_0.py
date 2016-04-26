# Ensure we have the correct version registered.
def Register(quiet):
    import win32com.servers.dictionary
    from win32com.test.util import RegisterPythonServer
    RegisterPythonServer(win32com.servers.dictionary.__file__, 'Python.Dictionary')
