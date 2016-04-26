###############################################################################
# Utility functions.
###############################################################################
def serve_udp(engine=None, port=9007, logto=sys.stdout):
    """Serve the `M2UDP` protocol using the given `engine` on the
    specified `port` logging messages to given `logto` which is a
    file-like object.  This function will block till the service is
    closed.  There is no need to call `mlab.show()` after or before
    this.  The Mayavi UI will be fully responsive.
    **Parameters**
     :engine: Mayavi engine to use. If this is `None`,
              `mlab.get_engine()` is used to find an appropriate engine.
     :port: int: port to serve on.
     :logto: file : File like object to log messages to.  If this is
                    `None` it disables logging.
    **Examples**
    Here is a very simple example::
        from mayavi import mlab
        from mayavi.tools import server
        mlab.test_plot3d()
        server.serve_udp()
    Test it like so::
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', 9008))
        s.sendto('camera.azimuth(10)', ('', 9007))
    **Warning**
    Data sent is exec'd so this is a security hole.
    """
    from mayavi import mlab
    e = engine or mlab.get_engine()
    # Setup the protocol with the right attributes.
    proto = M2UDP()
    proto.engine = e
    proto.scene = e.current_scene.scene
    proto.mlab = mlab
    if logto is not None:
        log.startLogging(logto)
    log.msg('Serving Mayavi2 UDP server on port', port)
    log.msg('Using Engine', e)
    # Register the running wxApp.
    reactor.registerWxApp(wx.GetApp())
    # Listen on port 9007 using above protocol.
    reactor.listenUDP(port, proto)
    # Run the server + app.  This will block.
    reactor.run()
