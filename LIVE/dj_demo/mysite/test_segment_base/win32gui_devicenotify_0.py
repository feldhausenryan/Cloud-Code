# WM_DEVICECHANGE message handler.
def OnDeviceChange(hwnd, msg, wp, lp):
    # Unpack the 'lp' into the appropriate DEV_BROADCAST_* structure,
    # using the self-identifying data inside the DEV_BROADCAST_HDR.
    info = win32gui_struct.UnpackDEV_BROADCAST(lp)
    print "Device change notification:", wp, str(info)
    if wp==win32con.DBT_DEVICEQUERYREMOVE and info.devicetype==win32con.DBT_DEVTYP_HANDLE:
        # Our handle is stored away in the structure - just close it
        print "Device being removed - closing handle"
        win32file.CloseHandle(info.handle)
        # and cancel our notifications - if it gets plugged back in we get
        # the same notification and try and close the same handle...
        win32gui.UnregisterDeviceNotification(info.hdevnotify)
    return True
