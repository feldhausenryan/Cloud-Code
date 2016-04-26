# Attempt to 're-execute' our current process with elevation.
def ReExecuteElevated(flags):
  from win32com.shell.shell import ShellExecuteEx
  from win32com.shell import shellcon
  import win32process, win32event
  import winxpgui # we've already checked we are running XP above
  import tempfile
  if not flags['quiet']:
    print "Requesting elevation and retrying..."
  new_params = " ".join(['"' + a + '"' for a in sys.argv])
  # If we aren't already in unattended mode, we want our sub-process to
  # be.
  if not flags['unattended']:
    new_params += " --unattended"
  # specifying the parent means the dialog is centered over our window,
  # which is a good usability clue.
  # hwnd is unlikely on the command-line, but flags may come from elsewhere
  hwnd = flags.get('hwnd', None)
  if hwnd is None:
    try:
      hwnd = winxpgui.GetConsoleWindow()
    except winxpgui.error:
      hwnd = 0
  # Redirect output so we give the user some clue what went wrong.  This
  # also means we need to use COMSPEC.  However, the "current directory"
  # appears to end up ignored - so we execute things via a temp batch file.
  tempbase = tempfile.mktemp("pycomserverreg")
  outfile = tempbase + ".out"
  batfile = tempbase + ".bat"
  # If registering from pythonwin, need to run python console instead since
  #  pythonwin will just open script for editting
  current_exe = os.path.split(sys.executable)[1].lower()
  exe_to_run = None
  if current_exe == 'pythonwin.exe':
    exe_to_run = os.path.join(sys.prefix, 'python.exe')
  elif current_exe == 'pythonwin_d.exe':
    exe_to_run = os.path.join(sys.prefix, 'python_d.exe')
  if not exe_to_run or not os.path.exists(exe_to_run):
    exe_to_run = sys.executable
  try:
    batf = open(batfile, "w")
    try:
      cwd = os.getcwd()
      print >> batf, "@echo off"
      # nothing is 'inherited' by the elevated process, including the
      # environment.  I wonder if we need to set more?
      print >> batf, "set PYTHONPATH=%s" % os.environ.get('PYTHONPATH', '')
      # may be on a different drive - select that before attempting to CD.
      print >> batf, os.path.splitdrive(cwd)[0]
      print >> batf, 'cd "%s"' % os.getcwd()
      print >> batf, '%s %s > "%s" 2>&1' % (win32api.GetShortPathName(exe_to_run), new_params, outfile)
    finally:
      batf.close()
    executable = os.environ.get('COMSPEC', 'cmd.exe')
    rc = ShellExecuteEx(hwnd=hwnd,
                        fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                        lpVerb="runas",
                        lpFile=executable,
                        lpParameters='/C "%s"' % batfile,
                        nShow=win32con.SW_SHOW)
    hproc = rc['hProcess']
    win32event.WaitForSingleObject(hproc, win32event.INFINITE)
    exit_code = win32process.GetExitCodeProcess(hproc)
    outf = open(outfile)
    try:
      output = outf.read()
    finally:
      outf.close()
    if exit_code:
      # Even if quiet you get to see this message.
      print "Error: registration failed (exit code %s)." % exit_code
    # if we are quiet then the output if likely to already be nearly
    # empty, so always print it.
    print output,
  finally:
    for f in (outfile, batfile):
      try:
        os.unlink(f)
      except os.error, exc:
        print "Failed to remove tempfile '%s': %s" % (f, exc)
