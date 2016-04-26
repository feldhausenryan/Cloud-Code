# Unpack an "LVNOTIFY" message
def UnpackLVDISPINFO(lparam):
    item_size = struct.calcsize(_lvitem_fmt)
    format = _nmhdr_fmt + _nmhdr_align_padding + ("%ds" % (item_size,))
    buf = win32gui.PyGetMemory(lparam, struct.calcsize(format))
    hwndFrom, id, code, buf_item = struct.unpack(format, buf)
    item = UnpackLVITEM(buf_item)
    return _MakeResult("LVDISPINFO hwndFrom id code item",
                       (hwndFrom, id, code, item))
