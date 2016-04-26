# The evt is set twice.  First when the server is ready to serve.
# Second when the server has been shutdown.  The user must clear
# the event after it has been set the first time to catch the second set.
def http_server(evt, numrequests, requestHandler=None):
    class TestInstanceClass:
        def div(self, x, y):
            return x // y
        def _methodHelp(self, name):
            if name == 'div':
                return 'This is the div function'
    def my_function():
        '''This is my function'''
        return True
    class MyXMLRPCServer(SimpleXMLRPCServer.SimpleXMLRPCServer):
        def get_request(self):
            # Ensure the socket is always non-blocking.  On Linux, socket
            # attributes are not inherited like they are on *BSD and Windows.
            s, port = self.socket.accept()
            s.setblocking(True)
            return s, port
    if not requestHandler:
        requestHandler = SimpleXMLRPCServer.SimpleXMLRPCRequestHandler
    serv = MyXMLRPCServer(("localhost", 0), requestHandler,
                          logRequests=False, bind_and_activate=False)
    try:
        serv.socket.settimeout(3)
        serv.server_bind()
        global ADDR, PORT, URL
        ADDR, PORT = serv.socket.getsockname()
        #connect to IP address directly.  This avoids socket.create_connection()
        #trying to connect to "localhost" using all address families, which
        #causes slowdown e.g. on vista which supports AF_INET6.  The server listens
        #on AF_INET only.
        URL = "http://%s:%d"%(ADDR, PORT)
        serv.server_activate()
        serv.register_introspection_functions()
        serv.register_multicall_functions()
        serv.register_function(pow)
        serv.register_function(lambda x,y: x+y, 'add')
        serv.register_function(my_function)
        serv.register_instance(TestInstanceClass())
        evt.set()
        # handle up to 'numrequests' requests
        while numrequests > 0:
            serv.handle_request()
            numrequests -= 1
    except socket.timeout:
        pass
    finally:
        serv.socket.close()
        PORT = None
        evt.set()
