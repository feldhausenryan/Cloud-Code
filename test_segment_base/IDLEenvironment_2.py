##	def __getattr__(self, attr):
##		if attr=="tk": return self # So text.tk.call works.
##		if attr=="master": return None # ditto!
##		raise AttributeError, attr
##	def __getitem__(self, item):
##		if item=="tabs":
##			size = self.edit.GetTabWidth()
##			if size==8: return "" # Tk default
##			return size # correct semantics?
##		elif item=="font": # Used for measurements we dont need to do!
##			return "Dont know the font"
##		raise IndexError, "Invalid index '%s'" % item
	def make_calltip_window(self):
		if self.calltips is None:
			self.calltips = CallTips(self.edit)
		return self.calltips
