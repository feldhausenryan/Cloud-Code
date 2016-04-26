# realpath is a no-op on systems without islink support
def realpath(path):
    path = abspath(path)
    try:
        import Carbon.File
    except ImportError:
        return path
    if not path:
        return path
    components = path.split(':')
    path = components[0] + ':'
    for c in components[1:]:
        path = join(path, c)
        try:
            path = Carbon.File.FSResolveAliasFile(path, 1)[0].as_pathname()
        except Carbon.File.Error:
            pass
    return path
