#		self.childListBoxID = childListBoxID
	def OnInitDialog(self):
		self.SetWindowText(self.title)
		self.hierList.HierInit(self)
		return dialog.Dialog.OnInitDialog(self)
