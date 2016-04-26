#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
def inputhook_glut():
    """Run the pyglet event loop by processing pending events only.
    This keeps processing pending events until stdin is ready.  After
    processing all pending events, a call to time.sleep is inserted.  This is
    needed, otherwise, CPU usage is at 100%.  This sleep time should be tuned
    though for best performance.
    """
    # We need to protect against a user pressing Control-C when IPython is
    # idle and this is running. We trap KeyboardInterrupt and pass.
    signal.signal(signal.SIGINT, glut_int_handler)
    try:
        t = clock()
        # Make sure the default window is set after a window has been closed
        if glut.glutGetWindow() == 0:
            glut.glutSetWindow( 1 )
            glutMainLoopEvent()
            return 0
        while not stdin_ready():
            glutMainLoopEvent()
            # We need to sleep at this point to keep the idle CPU load
            # low.  However, if sleep to long, GUI response is poor.  As
            # a compromise, we watch how often GUI events are being processed
            # and switch between a short and long sleep time.  Here are some
            # stats useful in helping to tune this.
            # time    CPU load
            # 0.001   13%
            # 0.005   3%
            # 0.01    1.5%
            # 0.05    0.5%
            used_time = clock() - t
            if used_time > 5*60.0:
                # print 'Sleep for 5 s'  # dbg
                time.sleep(5.0)
            elif used_time > 10.0:
                # print 'Sleep for 1 s'  # dbg
                time.sleep(1.0)
            elif used_time > 0.1:
                # Few GUI events coming in, so we can sleep longer
                # print 'Sleep for 0.05 s'  # dbg
                time.sleep(0.05)
            else:
                # Many GUI events coming in, so sleep only very little
                time.sleep(0.001)
    except KeyboardInterrupt:
        pass
    return 0
