#       def __del__(self):
#               print "DSFS dieing"
    def EnumStackFrames(self):
        trace("DebugStackFrameSniffer.EnumStackFrames called")
        return _wrap(EnumDebugStackFrames(self.debugger), axdebug.IID_IEnumDebugStackFrames)
