# fixme: WIP
def get_module_name_from_zip(filename):
    # first, find the zip file in the path
    filepath = filename
    zippath = None
    while not is_zipfile(filepath) and \
              splitdrive(filepath)[1] != '\\' \
              and splitdrive(filepath)[1] != '/':
        filepath, tail = os.path.split(filepath)
        if zippath is not None:
            zippath = tail + '/' + zippath
        else:
            zippath = tail
    if not is_zipfile(filepath):
        return None
    # if the split left a preceding slash on the zippath then remove
    # it
    if zippath.startswith('\\') or zippath.startswith('/'):
        zippath = zippath[1:]
    # replace any backwards slashes with forward slashes
    zippath = zippath.replace('\\', '/')
    # Get the name of the module minus the '.py'
    module, ext = splitext(basename(zippath))
    # Start with the actual module name.
    module_path = [module]
    # to get the module name, we walk through the zippath until we
    # find a parent directory that does NOT have a __init__.py file
    z = ZipFile(filepath)
    parentpath = dirname(zippath)
    while path_exists_in_zip(z, parentpath + '/__init__.py'):
        module_path.insert(0, basename(parentpath))
        parentpath = dirname(parentpath)
    z.close()
    return '.'.join(module_path)
