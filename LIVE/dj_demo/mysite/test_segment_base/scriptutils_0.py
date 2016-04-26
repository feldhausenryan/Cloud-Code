# Find the Python TabNanny in either the standard library or the Python Tools/Scripts directory.
def FindTabNanny():
	try:
		return __import__("tabnanny")
	except ImportError:
		pass
	# OK - not in the standard library - go looking.
	filename = "tabnanny.py"
	try:
		path = win32api.RegQueryValue(win32con.HKEY_LOCAL_MACHINE, "SOFTWARE\\Python\\PythonCore\\%s\\InstallPath" % (sys.winver))
	except win32api.error:
		print "WARNING - The Python registry does not have an 'InstallPath' setting"
		print "          The file '%s' can not be located" % (filename)
		return None
	fname = os.path.join(path, "Tools\\Scripts\\%s" % filename)
	try:
		os.stat(fname)
	except os.error:
		print "WARNING - The file '%s' can not be located in path '%s'" % (filename, path)
		return None
	tabnannyhome, tabnannybase = os.path.split(fname)
	tabnannybase = os.path.splitext(tabnannybase)[0]
	# Put tab nanny at the top of the path.
	sys.path.insert(0, tabnannyhome)
	try:
		return __import__(tabnannybase)
	finally:
		# remove the tab-nanny from the path
		del sys.path[0]
