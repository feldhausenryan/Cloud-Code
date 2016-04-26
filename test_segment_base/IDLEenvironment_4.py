######################################################################
# 
# Test related code.
# 
######################################################################
def TestCheck(index, edit, expected=None):
	rc = TkIndexToOffset(index, edit, {})
	if rc != expected:
		print "ERROR: Index", index,", expected", expected, "but got", rc
