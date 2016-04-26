###############################################################################
# Examples and tests.
###############################################################################
def test_tcp():
    """Simple test for the TCP server."""
    from mayavi import mlab
    mlab.test_plot3d()
    serve_tcp()
