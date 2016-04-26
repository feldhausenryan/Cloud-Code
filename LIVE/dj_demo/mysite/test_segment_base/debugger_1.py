# Prepare all the "control bars" for this package.
# If control bars are not all loaded when the toolbar-state functions are
# called, things go horribly wrong.
def PrepareControlBars(frame):
	style = win32con.WS_CHILD | afxres.CBRS_SIZE_DYNAMIC | afxres.CBRS_TOP | afxres.CBRS_TOOLTIPS | afxres.CBRS_FLYBY
	tbd = win32ui.CreateToolBar (frame, style, win32ui.ID_VIEW_TOOLBAR_DBG)
	tbd.ModifyStyle(0, commctrl.TBSTYLE_FLAT)
	tbd.LoadToolBar(win32ui.IDR_DEBUGGER)
	tbd.EnableDocking(afxres.CBRS_ALIGN_ANY)
	tbd.SetWindowText("Debugger")
	frame.DockControlBar(tbd)
	# and the other windows.
	for id, klass, float in DebuggerDialogInfos:
		try:
			frame.GetControlBar(id)
			exists=1
		except win32ui.error:
			exists=0
		if exists: continue
		bar = pywin.docking.DockingBar.DockingBar()
		style=win32con.WS_CHILD | afxres.CBRS_LEFT # don't create visible.
		bar.CreateWindow(frame, CreateDebuggerDialog, klass.title, id, style, childCreatorArgs=(klass,))
		bar.SetBarStyle( bar.GetBarStyle()|afxres.CBRS_TOOLTIPS|afxres.CBRS_FLYBY|afxres.CBRS_SIZE_DYNAMIC)
		bar.EnableDocking(afxres.CBRS_ALIGN_ANY)
		if float is None:
			frame.DockControlBar(bar)
		else:
			frame.FloatControlBar(bar, float, afxres.CBRS_ALIGN_ANY)
		## frame.ShowControlBar(bar, 0, 1)
