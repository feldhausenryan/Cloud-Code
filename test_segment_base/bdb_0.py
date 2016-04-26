# Determines if there is an effective (active) breakpoint at this
# line of code.  Returns breakpoint number or 0 if none
def effective(file, line, frame):
    """Determine which breakpoint for this file:line is to be acted upon.
    Called only if we know there is a bpt at this
    location.  Returns breakpoint that was triggered and a flag
    that indicates if it is ok to delete a temporary bp.
    """
    possibles = Breakpoint.bplist[file,line]
    for i in range(0, len(possibles)):
        b = possibles[i]
        if b.enabled == 0:
            continue
        if not checkfuncname(b, frame):
            continue
        # Count every hit when bp is enabled
        b.hits = b.hits + 1
        if not b.cond:
            # If unconditional, and ignoring,
            # go on to next, else break
            if b.ignore > 0:
                b.ignore = b.ignore -1
                continue
            else:
                # breakpoint and marker that's ok
                # to delete if temporary
                return (b,1)
        else:
            # Conditional bp.
            # Ignore count applies only to those bpt hits where the
            # condition evaluates to true.
            try:
                val = eval(b.cond, frame.f_globals,
                       frame.f_locals)
                if val:
                    if b.ignore > 0:
                        b.ignore = b.ignore -1
                        # continue
                    else:
                        return (b,1)
                # else:
                #   continue
            except:
                # if eval fails, most conservative
                # thing is to stop on breakpoint
                # regardless of ignore count.
                # Don't delete temporary,
                # as another hint to user.
                return (b,0)
    return (None, None)
