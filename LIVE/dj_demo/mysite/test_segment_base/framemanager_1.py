# Convenience function
def AuiManager_UseNativeMiniframes(manager):
    """
    Static function which returns if the input `manager` should use native :class:`MiniFrame` as
    floating panes.
    :param `manager`: an instance of :class:`AuiManager`.
    .. note::
       This method always returns ``True`` on wxMAC as this platform doesn't have
       the ability to use custom drawn miniframes.
    """
    # With Core Graphics on Mac, it's not possible to show sash feedback,
    # so we'll always use live update instead.
    if wx.Platform == "__WXMAC__":
        return True
    else:
        return (manager.GetAGWFlags() & AUI_MGR_USE_NATIVE_MINIFRAMES) == AUI_MGR_USE_NATIVE_MINIFRAMES
