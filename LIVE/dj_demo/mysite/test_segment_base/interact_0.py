# The factory we pass to the dockable window support.
def InteractiveViewCreator(parent):
	global edit
	edit = CDockedInteractivePython(parent)
	return edit.currentView
