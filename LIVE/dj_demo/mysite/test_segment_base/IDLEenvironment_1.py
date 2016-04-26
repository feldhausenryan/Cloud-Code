########################################
#
# Helpers for the TkText emulation.
def TkOffsetToIndex(offset, edit):
	lineoff = 0
	# May be 1 > actual end if we pretended there was a trailing '\n'
	offset = min(offset, edit.GetTextLength())
	line = edit.LineFromChar(offset)
	lineIndex = edit.LineIndex(line)
	return "%d.%d" % (line+1, offset-lineIndex)
