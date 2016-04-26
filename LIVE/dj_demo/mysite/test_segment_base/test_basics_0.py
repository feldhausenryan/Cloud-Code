# The worker function for the subprocess (needs to be here because Windows
# has problems pickling nested functions with the multiprocess module :-/)
def _worker(fn, qout = None):
    fp = tables.openFile(fn)
    if common.verbose:
        print "About to load: ", fn
    rows = fp.root.table.where('(f0 < 10)')
    if common.verbose:
        print "Got the iterator, about to iterate"
    next(rows)
    if common.verbose:
        print "Succeeded in one iteration\n"
    fp.close()
    if qout is not None:
        qout.put("Done")
