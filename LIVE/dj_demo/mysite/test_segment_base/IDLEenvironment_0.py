# A class that is injected into the IDLE auto-indent extension.
# It allows for decent performance when opening a new file,
# as auto-indent uses the tokenizer module to determine indents.
# The default AutoIndent readline method works OK, but it goes through
# this layer of Tk index indirection for every single line.  For large files
# without indents (and even small files with indents :-) it was pretty slow!
def fast_readline(self):
	if self.finished:
		val = ""
	else:
		if "_scint_lines" not in self.__dict__:
			# XXX - note - assumes this is only called once the file is loaded!
			self._scint_lines = self.text.edit.GetTextRange().split("\n")
		sl = self._scint_lines
		i = self.i = self.i + 1
		if i >= len(sl):
			val = ""
		else:
			val = sl[i]+"\n"
	return val.encode(default_scintilla_encoding)
