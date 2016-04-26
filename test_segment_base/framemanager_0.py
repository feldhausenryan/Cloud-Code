# Convenience function
def AuiManager_HasLiveResize(manager):
    """
    Static function which returns if the input `manager` should have "live resize"
    behaviour.
    :param `manager`: an instance of :class:`AuiManager`.
    .. note::
       This method always returns ``True`` on wxMAC as this platform doesn't have
       the ability to use :class:`ScreenDC` to draw sashes.
    """
    # With Core Graphics on Mac, it's not possible to show sash feedback,
    # so we'll always use live update instead.
    if wx.Platform == "__WXMAC__":
        return True
    else:
        return (manager.GetAGWFlags() & AUI_MGR_LIVE_RESIZE) == AUI_MGR_LIVE_RESIZE
