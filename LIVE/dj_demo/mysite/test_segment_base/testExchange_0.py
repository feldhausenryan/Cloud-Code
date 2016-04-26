#
# Recursive dump of folders.
#
def DumpFolder(folder, indent = 0):
    print " " * indent, folder.Name
    folders = folder.Folders
    folder = folders.GetFirst()
    while folder:
        DumpFolder(folder, indent+1)
        folder = folders.GetNext()
