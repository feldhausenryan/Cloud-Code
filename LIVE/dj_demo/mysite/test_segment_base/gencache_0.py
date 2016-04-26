#
# The helpers for win32com.client.Dispatch and OCX clients.
#
def GetClassForProgID(progid):
	"""Get a Python class for a Program ID
	Given a Program ID, return a Python class which wraps the COM object
	Returns the Python class, or None if no module is available.
	Params
	progid -- A COM ProgramID or IID (eg, "Word.Application")
	"""
	clsid = pywintypes.IID(progid) # This auto-converts named to IDs.
	return GetClassForCLSID(clsid)
