# Some code that actually uses these objects.
def demo(modal = 0):
	TestDialog(modal)
	# property sheet/page demo
	ps=win32ui.CreatePropertySheet('Property Sheet/Page Demo')
	# Create a completely standard PropertyPage.
	page1=win32ui.CreatePropertyPage(win32ui.IDD_PROPDEMO1)
	# Create our custom property page.
	page2=TestPage(win32ui.IDD_PROPDEMO2)
	ps.AddPage(page1)
	ps.AddPage(page2)
	if modal:
		ps.DoModal()
	else:
		style = win32con.WS_SYSMENU|win32con.WS_POPUP|win32con.WS_CAPTION|win32con.DS_MODALFRAME|win32con.WS_VISIBLE
		styleex = win32con.WS_EX_DLGMODALFRAME | win32con.WS_EX_PALETTEWINDOW
		ps.CreateWindow(win32ui.GetMainFrame(), style, styleex)
