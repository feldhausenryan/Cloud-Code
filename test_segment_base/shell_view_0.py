# Helper function to get a system IShellFolder interface, and the PIDL within
# that folder for an existing file/directory.
def GetFolderAndPIDLForPath(filename):
    desktop = shell.SHGetDesktopFolder()
    info = desktop.ParseDisplayName(0, None, os.path.abspath(filename))
    cchEaten, pidl, attr = info
    # We must walk the ID list, looking for one child at a time.
    folder = desktop
    while len(pidl) > 1:
        this = pidl.pop(0)
        folder = folder.BindToObject([this], None, shell.IID_IShellFolder)
    # We are left with the pidl for the specific item.  Leave it as
    # a list, so it remains a valid PIDL.
    return folder, pidl
