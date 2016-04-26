# Unpack the lparm from a "TVNOTIFY" message
def UnpackTVNOTIFY(lparam):
    item_size = struct.calcsize(_tvitem_fmt)
    format = _nmhdr_fmt + _nmhdr_align_padding
    if is64bit:
        format = format + "ixxxx"
    else:
        format = format + "i"
    format = format + "%ds%ds" % (item_size, item_size)
    buf = win32gui.PyGetMemory(lparam, struct.calcsize(format))
    hwndFrom, id, code, action, buf_old, buf_new \
          = struct.unpack(format, buf)
    item_old = UnpackTVITEM(buf_old)
    item_new = UnpackTVITEM(buf_new)
    return _MakeResult("TVNOTIFY hwndFrom id code action item_old item_new",
                       (hwndFrom, id, code, action, item_old, item_new))
