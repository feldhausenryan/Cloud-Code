######################################################################
def check_backend():
    """ Check if either we are in test mode, or if there is a
        suitable traits backend installed.
    """
    from traitsui.toolkit import toolkit
    from traits.etsconfig.api import ETSConfig
    from mayavi.tools.engine_manager import options
    toolkit()  # This forces the selection of a toolkit.
    if (options.backend != 'test' and options.offscreen != True) and \
            ETSConfig.toolkit in ('null', ''):
        raise ImportError('''Could not import backend for traits
