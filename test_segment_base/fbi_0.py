# Insert a call to this function into your program to invoke the debugger:
def bp ( condition = True ):
    if condition:
        fbi_bdb.set_trace()
