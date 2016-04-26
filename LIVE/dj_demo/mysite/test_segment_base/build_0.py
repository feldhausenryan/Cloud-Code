# It isn't really clear what the quoting rules are in a C/IDL string and
# literals like a quote char and backslashes makes life a little painful to
# always render the string perfectly - so just punt and fall-back to a repr()
def _makeDocString(s):
	if sys.version_info < (3,):
		s = s.encode("mbcs")
	return repr(s)
