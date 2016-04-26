# Helper for writing a Window position by name, and later loading it.
def SaveWindowSize(section,rect,state=""):
	""" Writes a rectangle to an INI file
	Args: section = section name in the applications INI file
	      rect = a rectangle in a (cy, cx, y, x) tuple 
	             (same format as CREATESTRUCT position tuples)."""	
	left, top, right, bottom = rect
	if state: state = state + " "
	win32ui.WriteProfileVal(section,state+"left",left)
	win32ui.WriteProfileVal(section,state+"top",top)
	win32ui.WriteProfileVal(section,state+"right",right)
	win32ui.WriteProfileVal(section,state+"bottom",bottom)
