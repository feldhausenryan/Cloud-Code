# The default items should no tools menu exist in the INI file.
defaultToolMenuItems = [
	('Browser', 'win32ui.GetApp().OnViewBrowse(0,0)'),
	('Browse PythonPath', 'from pywin.tools import browseProjects;browseProjects.Browse()'),
	('Edit Python Path', 'from pywin.tools import regedit;regedit.EditRegistry()'),
	('COM Makepy utility', 'from win32com.client import makepy;makepy.main()'),
	('COM Browser', 'from win32com.client import combrowse;combrowse.main()'),
	('Trace Collector Debugging tool', 'from pywin.tools import TraceCollector;TraceCollector.MakeOutputWindow()'),
