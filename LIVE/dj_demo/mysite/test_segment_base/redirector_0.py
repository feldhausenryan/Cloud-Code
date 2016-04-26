# An "io completion" function, called when ecb.ExecURL completes...
def io_callback(ecb, url, cbIO, errcode):
    # Get the status of our ExecURL
    httpstatus, substatus, win32 = ecb.GetExecURLStatus()
    print "ExecURL of %r finished with http status %d.%d, win32 status %d (%s)" % (
           url, httpstatus, substatus, win32, win32api.FormatMessage(win32).strip())
    # nothing more to do!
    ecb.DoneWithSession()
