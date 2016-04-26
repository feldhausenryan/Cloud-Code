# timer callback
def timer(msecs):
    global timeout
    timeout = msecs
    print 'Timer callback msecs:', msecs
