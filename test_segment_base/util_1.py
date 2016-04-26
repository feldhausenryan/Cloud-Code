# fixme: WIP
def path_exists_in_zip(zfile, path):
    try:
        zfile.getinfo(path)
        exists = True
    except:
        exists = False
    return exists
