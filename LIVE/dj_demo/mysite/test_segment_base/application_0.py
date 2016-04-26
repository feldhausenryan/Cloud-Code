#------------------------------------------------------------------------------
# Helper Functions
#------------------------------------------------------------------------------
def deferred_call(callback, *args, **kwargs):
    """ Invoke a callable on the next cycle of the main event loop
    thread.
    This is a convenience function for invoking the same method on the
    current application instance. If an application instance does not
    exist, a RuntimeError will be raised.
    Parameters
    ----------
    callback : callable
        The callable object to execute at some point in the future.
    *args, **kwargs
        Any additional positional and keyword arguments to pass to
        the callback.
    """
    app = Application.instance()
    if app is None:
        raise RuntimeError('Application instance does not exist')
    app.deferred_call(callback, *args, **kwargs)
