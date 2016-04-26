#       def _query_interface_(self, iid):
#               from win32com.util import IIDToInterfaceName
#               print "EnumDebugStackFrames QI with %s (%s)" % (IIDToInterfaceName(iid), str(iid))
#               return 0
    def _wrap(self, obj):
        # This enum returns a tuple, with 2 com objects in it.
        obFrame, min, lim, fFinal, obFinal = obj
        obFrame = _wrap(obFrame, axdebug.IID_IDebugStackFrame)
        if obFinal:
            obFinal = _wrap(obFinal, pythoncom.IID_IUnknown)
        return obFrame, min, lim, fFinal, obFinal
