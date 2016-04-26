# This verifies that you can't set f_lineno via _getframe or similar
# trickery.
def no_jump_without_trace_function():
    try:
        previous_frame = sys._getframe().f_back
        previous_frame.f_lineno = previous_frame.f_lineno
    except ValueError, e:
        # This is the exception we wanted; make sure the error message
        # talks about trace functions.
        if 'trace' not in str(e):
            raise
    else:
        # Something's wrong - the expected exception wasn't raised.
        raise RuntimeError, "Trace-function-less jump failed to fail"
