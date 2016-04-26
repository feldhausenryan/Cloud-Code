#       def __del__(self):
#               print "DSF dieing"
    def _query_interface_(self, iid):
        if iid==axdebug.IID_IDebugExpressionContext:
            if self.expressionContext is None:
                self.expressionContext = _wrap(expressions.ExpressionContext(self.frame), axdebug.IID_IDebugExpressionContext)
            return self.expressionContext
#               from win32com.util import IIDToInterfaceName
#               print "DebugStackFrame QI with %s (%s)" % (IIDToInterfaceName(iid), str(iid))
        return 0
