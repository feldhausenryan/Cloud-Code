# Allow the set_trace code to operate outside of an ipython instance, even if
# it does so with some limitations.  The rest of this support is implemented in
# the Tracer constructor.
def BdbQuit_excepthook(et, ev, tb, excepthook=None):
    """Exception hook which handles `BdbQuit` exceptions.
    All other exceptions are processed using the `excepthook`
    parameter.
    """
    if et==bdb.BdbQuit:
        print 'Exiting Debugger.'
    elif excepthook is not None:
        excepthook(et, ev, tb)
    else:
        # Backwards compatibility. Raise deprecation warning?
        BdbQuit_excepthook.excepthook_ori(et,ev,tb)
