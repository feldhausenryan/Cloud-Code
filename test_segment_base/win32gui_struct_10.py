# Support for unpacking the 'lparam'    
def UnpackDEV_BROADCAST(lparam):
    if lparam == 0:
        return None
    hdr_format = "iii"
    hdr_size = struct.calcsize(hdr_format)
    hdr_buf = win32gui.PyGetMemory(lparam, hdr_size)
    size, devtype, reserved = struct.unpack("iii", hdr_buf)
    # Due to x64 alignment issues, we need to use the full format string over
    # the entire buffer.  ie, on x64:
    # calcsize('iiiP') != calcsize('iii')+calcsize('P')
    buf = win32gui.PyGetMemory(lparam, size)
    extra = x = {}
    if devtype == win32con.DBT_DEVTYP_HANDLE:
        # 2 handles, a GUID, a LONG and possibly an array following...
        fmt = hdr_format + "PP16sl"
        _, _, _, x['handle'], x['hdevnotify'], guid_bytes, x['nameoffset'] = \
            struct.unpack(fmt, buf[:struct.calcsize(fmt)])
        x['eventguid'] = pywintypes.IID(guid_bytes, True)
    elif devtype == win32con.DBT_DEVTYP_DEVICEINTERFACE:
        fmt = hdr_format + "16s"
        _, _, _, guid_bytes = struct.unpack(fmt, buf[:struct.calcsize(fmt)])
        x['classguid'] = pywintypes.IID(guid_bytes, True)
        x['name'] = win32gui.PyGetString(lparam + struct.calcsize(fmt))
    elif devtype == win32con.DBT_DEVTYP_VOLUME:
        # int mask and flags
        fmt = hdr_format + "II"
        _, _, _, x['unitmask'], x['flags'] = struct.unpack(fmt, buf[:struct.calcsize(fmt)])
    else:
        raise NotImplementedError("unknown device type %d" % (devtype,))
    return DEV_BROADCAST_INFO(devtype, **extra)
