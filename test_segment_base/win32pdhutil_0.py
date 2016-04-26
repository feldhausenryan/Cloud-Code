# NOTE: This BrowseCallback doesn't seem to work on Vista for markh.
# XXX - look at why!?
# Some counters on Vista require elevation, and callback would previously
# clear exceptions without printing them.
def BrowseCallBackDemo(counters):
    ## BrowseCounters can now return multiple counter paths
    for counter in counters:
        machine, object, instance, parentInstance, index, counterName = \
                win32pdh.ParseCounterPath(counter)
        result = GetPerformanceAttributes(object, counterName, instance, index,
                                          win32pdh.PDH_FMT_DOUBLE, machine)
        print "Value of '%s' is" % counter, result
        print "Added '%s' on object '%s' (machine %s), instance %s(%d)-parent of %s" \
              % (counterName, object, machine, instance, index, parentInstance)
    return 0
