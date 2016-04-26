# socket callback
def socket(event, socket, multi, data):
    if event == pycurl.POLL_REMOVE:
        print "Remove Socket %d"%socket
        sockets.remove(socket)
    else:
        if socket not in sockets:
            print "Add socket %d"%socket
            sockets.add(socket)
    print event, socket, multi, data
