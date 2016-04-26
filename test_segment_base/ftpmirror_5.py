# Create a directory if it doesn't exist.  Recursively create the
# parent directory as well if needed.
def makedir(pathname):
    if os.path.isdir(pathname):
        return
    dirname = os.path.dirname(pathname)
    if dirname: makedir(dirname)
    os.mkdir(pathname, 0777)
