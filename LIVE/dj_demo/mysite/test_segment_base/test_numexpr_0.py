# The worker function for the subprocess (needs to be here because Windows
# has problems pickling nested functions with the multiprocess module :-/)
def _worker(qout = None):
    ra = numpy.arange(1e3)
    rows = evaluate('ra > 0')
    #print "Succeeded in evaluation!\n"
    if qout is not None:
        qout.put("Done")
