#-----------------------------------------------------------------------------
# Functions and classes
#-----------------------------------------------------------------------------
def pylab_kernel(gui):
    """Launch and return an IPython kernel with pylab support for the desired gui
    """
    kernel = IPKernelApp.instance()
    kernel.initialize(['python', '--pylab=%s' % gui,
                       #'--log-level=10'
                       ])
    return kernel
