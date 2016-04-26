# Test a few of the MSOffice components.
def TestWord():
    # Try and load the object exposed by Word 8
    # Office 97 - _totally_ different object model!
    try:
        # NOTE - using "client.Dispatch" would return an msword8.py instance!
        print "Starting Word 8 for dynamic test"
        word = win32com.client.dynamic.Dispatch("Word.Application")
        TestWord8(word)
        word = None
        # Now we will test Dispatch without the new "lazy" capabilities
        print "Starting Word 8 for non-lazy dynamic test"
        dispatch = win32com.client.dynamic._GetGoodDispatch("Word.Application")
        typeinfo = dispatch.GetTypeInfo()
        attr = typeinfo.GetTypeAttr()
        olerepr = win32com.client.build.DispatchItem(typeinfo, attr, None, 0)
        word = win32com.client.dynamic.CDispatch(dispatch, olerepr)
        dispatch = typeinfo = attr = olerepr = None
        TestWord8(word)
    except pythoncom.com_error:
        print "Starting Word 7 for dynamic test"
        word = win32com.client.Dispatch("Word.Basic")
        TestWord7(word)
    print "Starting MSWord for generated test"
    from win32com.client import gencache
    word = gencache.EnsureDispatch("Word.Application.8")
    TestWord8(word)
