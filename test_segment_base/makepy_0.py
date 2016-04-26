"""

import sys, os, pythoncom
from win32com.client import genpy, selecttlb, gencache
from win32com.client import Dispatch

bForDemandDefault = 0 # Default value of bForDemand - toggle this to change the world - see also gencache.py

error = "makepy.error"

def usage():
	sys.stderr.write (usageHelp)
	sys.exit(2)

def ShowInfo(spec):
	if not spec:
		tlbSpec = selecttlb.SelectTlb(excludeFlags=selecttlb.FLAG_HIDDEN)
		if tlbSpec is None:
			return
		try:
			tlb = pythoncom.LoadRegTypeLib(tlbSpec.clsid, tlbSpec.major, tlbSpec.minor, tlbSpec.lcid)
		except pythoncom.com_error: # May be badly registered.
			sys.stderr.write("Warning - could not load registered typelib '%s'\n" % (tlbSpec.clsid))
			tlb = None
		
		infos = [(tlb, tlbSpec)]
	else:
		infos = GetTypeLibsForSpec(spec)
	for (tlb, tlbSpec) in infos:
		desc = tlbSpec.desc
		if desc is None:
			if tlb is None:
				desc = "<Could not load typelib %s>" % (tlbSpec.dll)
			else:
				desc = tlb.GetDocumentation(-1)[0]
		print desc
		print " %s, lcid=%s, major=%s, minor=%s" % (tlbSpec.clsid, tlbSpec.lcid, tlbSpec.major, tlbSpec.minor)
		print " >>> # Use these commands in Python code to auto generate .py support"
		print " >>> from win32com.client import gencache"
		print " >>> gencache.EnsureModule('%s', %s, %s, %s)" % (tlbSpec.clsid, tlbSpec.lcid, tlbSpec.major, tlbSpec.minor)

class SimpleProgress(genpy.GeneratorProgress):
	"""A simple progress class prints its output to stderr
	"""
	def __init__(self, verboseLevel):
		self.verboseLevel = verboseLevel
