# Gets/Sets the default DockWindow theme:
def dock_window_theme ( theme = None ):
    global _dock_window_theme
    if _dock_window_theme is None:
        from .default_dock_window_theme import default_dock_window_theme
        _dock_window_theme = default_dock_window_theme
    old_theme = _dock_window_theme
    if theme is not None:
        _dock_window_theme = theme
    return old_theme
