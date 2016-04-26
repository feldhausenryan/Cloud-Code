# Generic WM_NOTIFY unpacking
def UnpackWMNOTIFY(lparam):
    format = "PPi"
    buf = win32gui.PyGetMemory(lparam, struct.calcsize(format))
    return _MakeResult("WMNOTIFY hwndFrom idFrom code", struct.unpack(format, buf))
