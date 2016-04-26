###############################
##
## Some vtable tests of the interface
##
def TestVTable(clsctx=pythoncom.CLSCTX_ALL):
    # Any vtable interfaces marked as dual *should* be able to be
    # correctly implemented as IDispatch.
    ob = win32com.client.Dispatch("Python.Test.PyCOMTest")
    TestLocalVTable(ob)
    # Now test it via vtable - use some C++ code to help here as Python can't do it directly yet.
    tester = win32com.client.Dispatch("PyCOMTest.PyCOMTest")
    testee = pythoncom.CoCreateInstance("Python.Test.PyCOMTest", None, clsctx, pythoncom.IID_IUnknown)
    # check we fail gracefully with None passed.
    try:
        tester.TestMyInterface(None)
    except pythoncom.com_error, details:
        pass
    # and a real object.
    tester.TestMyInterface(testee)
