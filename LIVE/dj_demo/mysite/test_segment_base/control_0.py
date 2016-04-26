#	def SCIColourise(self, start=0, end=-1):
#   NOTE - dependent on of we use builtin lexer, so handled below.		
	def SCIGetEndStyled(self):
		return self.SendScintilla(scintillacon.SCI_GETENDSTYLED)
