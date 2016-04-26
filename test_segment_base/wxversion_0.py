# Scan the sys.path looking for either a directory matching _pattern,
# or a wx.pth file
def _find_default():
    for pth in sys.path:
        # empty means to look in the current dir
        if not pth:
            pth = '.'
        # skip it if it's not a package dir
        if not os.path.isdir(pth):
            continue
        # does it match the pattern?
        base = os.path.basename(pth)
        if fnmatch.fnmatchcase(base, _pattern):
            return pth
    for pth in sys.path:
        if not pth:
            pth = '.'
        if not os.path.isdir(pth):
            continue
        if os.path.exists(os.path.join(pth, 'wx.pth')):
            base = open(os.path.join(pth, 'wx.pth')).read()
            return os.path.join(pth, base)
    return None
