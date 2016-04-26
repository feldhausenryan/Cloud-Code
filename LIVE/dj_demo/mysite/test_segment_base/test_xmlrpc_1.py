# This function prevents errors like:
#    <ProtocolError for localhost:57527/RPC2: 500 Internal Server Error>
def is_unavailable_exception(e):
    '''Returns True if the given ProtocolError is the product of a server-side
       exception caused by the 'temporarily unavailable' response sometimes
       given by operations on non-blocking sockets.'''
    # sometimes we get a -1 error code and/or empty headers
    try:
        if e.errcode == -1 or e.headers is None:
            return True
        exc_mess = e.headers.get('X-exception')
    except AttributeError:
        # Ignore socket.errors here.
        exc_mess = str(e)
    if exc_mess and 'temporarily unavailable' in exc_mess.lower():
        return True
    return False
