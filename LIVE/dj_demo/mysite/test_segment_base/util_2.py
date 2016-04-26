# fixme: WIP
def is_zip_path(path):
    """ Returns True if the path refers to a zip file. """
    filepath = path
    while not is_zipfile(filepath) and \
              splitdrive(filepath)[1] != '\\' \
              and splitdrive(filepath)[1] != '/':
        filepath = dirname(filepath)
    return is_zipfile(filepath)
