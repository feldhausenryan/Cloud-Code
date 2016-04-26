####################################
#
# Video Control
#
def GetTestVideoModule():
	global videoControlModule, videoControlFileName
	win32ui.DoWaitCursor(1)
	videoControlModule = gencache.EnsureModule("{05589FA0-C356-11CE-BF01-00AA0055595A}", 0, 2, 0)
	win32ui.DoWaitCursor(0)
	if videoControlModule is None:
		return None
	fnames = glob.glob(os.path.join(win32api.GetWindowsDirectory(), "*.avi"))
	if not fnames:
		print "No AVI files available in system directory"
		return None
	videoControlFileName = fnames[0]
	return videoControlModule
