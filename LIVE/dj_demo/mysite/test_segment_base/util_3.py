# fixme: WIP
def get_zip_path(filename):
    """ Returns the path to the zip file contained in the filename.
    fixme: An example here would help.
    """
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
    return zippath
