# The signal handler. Just note that the signal occurred and
# from who.
def handle_signals(sig,frame):
    signal_blackboard[sig]['tripped'] += 1
    signal_blackboard[sig]['tripped_by'] = thread.get_ident()
