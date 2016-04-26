# start of Utils.cpp port
def DisplayItem(shell_item_array, hwnd_parent=0):
    # Get the first ShellItem and display its name
    if shell_item_array is None:
        msg = "You must select something!"
    else:
        si = shell_item_array.GetItemAt(0)
        name = si.GetDisplayName(shellcon.SIGDN_NORMALDISPLAY)
        msg = "%d items selected, first is %r" % (shell_item_array.GetCount(), name)
    win32gui.MessageBox(hwnd_parent, msg, "Hello", win32con.MB_OK)
