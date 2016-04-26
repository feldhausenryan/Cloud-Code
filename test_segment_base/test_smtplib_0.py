# Test server thread using the specified SMTP server class
def debugging_server(serv, serv_evt, client_evt):
    serv_evt.set()
    try:
        if hasattr(select, 'poll'):
            poll_fun = asyncore.poll2
        else:
            poll_fun = asyncore.poll
        n = 1000
        while asyncore.socket_map and n > 0:
            poll_fun(0.01, asyncore.socket_map)
            # when the client conversation is finished, it will
            # set client_evt, and it's then ok to kill the server
            if client_evt.is_set():
                serv.close()
                break
            n -= 1
    except socket.timeout:
        pass
    finally:
        if not client_evt.is_set():
            # allow some time for the client to read the result
            time.sleep(0.5)
            serv.close()
        asyncore.close_all()
        serv_evt.set()
