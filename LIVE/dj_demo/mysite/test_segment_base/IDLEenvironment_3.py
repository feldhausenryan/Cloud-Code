##	def get_tab_width(self):
##		return self.edit.GetTabWidth()
##	def call(self, *rest):
##		# Crap to support Tk measurement hacks for tab widths
##		if rest[0] != "font" or rest[1] != "measure":
##			raise ValueError, "Unsupport call type"
##		return len(rest[5])
##	def configure(self, **kw):
##		for name, val in kw.items():
##			if name=="tabs":
##				self.edit.SCISetTabWidth(int(val))
##			else:
##				raise ValueError, "Unsupported configuration item %s" % kw
	def bind(self, binding, handler):
		self.edit.bindings.bind(binding, handler)
