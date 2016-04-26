# XXX: handle cross compilation
def is_win64():
    return sys.platform == "win32" and platform.architecture()[0] == "64bit"
