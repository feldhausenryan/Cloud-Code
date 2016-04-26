# If a user hits ^C during a run, it is wise to gracefully close the opened files.
def close_open_files():
    are_open_files = len(_open_files) > 0
    if are_open_files:
        print >> sys.stderr, "Closing remaining open files:",
    for fname, fileh in _open_files.items():
        print >> sys.stderr, "%s..." % (fname,),
        fileh.close()
        print >> sys.stderr, "done",
    if are_open_files:
        print >> sys.stderr
