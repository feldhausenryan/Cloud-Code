# We need a little factory function here to create the closure where
# safe_execfile can live.
def mpl_runner(safe_execfile):
    """Factory to return a matplotlib-enabled runner for %run.
    Parameters
    ----------
    safe_execfile : function
      This must be a function with the same interface as the
      :meth:`safe_execfile` method of IPython.
    Returns
    -------
    A function suitable for use as the ``runner`` argument of the %run magic
    function.
    """
    def mpl_execfile(fname,*where,**kw):
        """matplotlib-aware wrapper around safe_execfile.
        Its interface is identical to that of the :func:`execfile` builtin.
        This is ultimately a call to execfile(), but wrapped in safeties to
        properly handle interactive rendering."""
        import matplotlib
        import matplotlib.pylab as pylab
        #print '*** Matplotlib runner ***' # dbg
        # turn off rendering until end of script
        is_interactive = matplotlib.rcParams['interactive']
        matplotlib.interactive(False)
        safe_execfile(fname,*where,**kw)
        matplotlib.interactive(is_interactive)
        # make rendering call now, if the user tried to do it
        if pylab.draw_if_interactive.called:
            pylab.draw()
            pylab.draw_if_interactive.called = False
    return mpl_execfile
