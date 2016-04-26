# Convenience function to switch amongst them
def enable_gui(gui=None, app=None):
    r"""Switch amongst GUI input hooks by name.
    This is just a utility wrapper around the methods of the InputHookManager
    object.
    Parameters
    ----------
    gui : string or None, optional
        If None (or 'none'), clears input hook, otherwise it must be one
        of the recognized GUI names (see ``GUI\_\*`` constants in module).
    app : existing application object, optional
        For toolkits that have the concept of a global app, you can supply an
        existing one.  If not given, the toolkit will be probed for one, and if
        none is found, a new one will be created.  Note that GTK does not have
        this concept, and passing an app if ``gui=="GTK"`` will raise an error.
    Returns
    -------
    inputhook_result : an object
        The output of the underlying gui switch routine, typically the actual
        PyOS_InputHook wrapper object or the GUI toolkit app created, if there was
        one.
    """
    guis = {None: clear_inputhook,
            GUI_NONE: clear_inputhook,
            GUI_OSX: lambda app=False: None,
            GUI_TK: enable_tk,
            GUI_GTK: enable_gtk,
            GUI_WX: enable_wx,
            GUI_QT: enable_qt4, # qt3 not supported
            GUI_QT4: enable_qt4,
            GUI_GLUT: enable_glut,
            GUI_PYGLET: enable_pyglet,
            GUI_GTK3: enable_gtk3,
            }
    try:
        gui_hook = guis[gui]
    except KeyError:
        e = "Invalid GUI request %r, valid ones are:%s" % (gui, guis.keys())
        raise ValueError(e)
    return gui_hook(app)
