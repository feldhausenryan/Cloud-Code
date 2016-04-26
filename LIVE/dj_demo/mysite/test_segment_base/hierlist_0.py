# helper to get the text of an arbitary item
def GetItemText(item):
	if type(item)==type(()) or type(item)==type([]):
		use = item[0]
	else:
		use = item
	if type(use)==type(''):
		return use
	else:
		return repr(item)
