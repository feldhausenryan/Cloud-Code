# Insert a call to this function into your program to invoke the debugger if
# the FBI is enabled:
def if_bp ( condition = True ):
    global fbi_enabled
    if fbi_enabled and condition:
        fbi_bdb.set_trace()
    return fbi_enabled
