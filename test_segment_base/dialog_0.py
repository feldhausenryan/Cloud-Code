# define some app utility functions.
def GetSimpleInput(prompt, defValue='', title=None ):
	""" displays a dialog, and returns a string, or None if cancelled.
	args prompt, defValue='', title=main frames title """
	# uses a simple dialog to return a string object.
	if title is None: title=win32ui.GetMainFrame().GetWindowText()
	# 2to3 insists on converting 'Dialog.__init__' to 'tkinter.dialog...'
	DlgBaseClass = Dialog
	class DlgSimpleInput(DlgBaseClass):
		def __init__(self, prompt, defValue, title ):
			self.title=title
			DlgBaseClass.__init__(self, win32ui.IDD_SIMPLE_INPUT)
			self.AddDDX(win32ui.IDC_EDIT1,'result')
			self.AddDDX(win32ui.IDC_PROMPT1, 'prompt')
			self._obj_.data['result']=defValue
			self._obj_.data['prompt']=prompt
		def OnInitDialog(self):
			self.SetWindowText(self.title)
			return DlgBaseClass.OnInitDialog(self)
	dlg=DlgSimpleInput( prompt, defValue, title)
	if dlg.DoModal() != win32con.IDOK:
		return None
	return dlg['result']
