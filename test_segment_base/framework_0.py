# Make sure we have a valid sys.stdout/stderr, otherwise out
# print and trace statements may raise an exception
def MakeValidSysOuts():
	if not isinstance(sys.stdout, SafeOutput):
		sys.stdout = sys.stderr = SafeOutput()
		# and for the sake of working around something I can't understand...
		# prevent keyboard interrupts from killing IIS
		import signal
		def noOp(a,b):
			# it would be nice to get to the bottom of this, so a warning to
			# the debug console can't hurt.
			print "WARNING: Ignoring keyboard interrupt from ActiveScripting engine"
		# If someone else has already redirected, then assume they know what they are doing!
		if signal.getsignal(signal.SIGINT) == signal.default_int_handler:
			try:
				signal.signal(signal.SIGINT, noOp)
			except ValueError:
				# Not the main thread - can't do much.
				pass
