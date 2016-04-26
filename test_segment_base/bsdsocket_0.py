# * Old com implementation *
# See solution (1) in Issue 434:
# http://code.google.com/p/spyderlib/issues/detail?id=434#c13
def communicate(sock, command, settings=[]):
    """Communicate with monitor"""
    try:
        COMMUNICATE_LOCK.acquire()
        write_packet(sock, command)
        for option in settings:
            write_packet(sock, option)
        return read_packet(sock)
    finally:
        COMMUNICATE_LOCK.release()
