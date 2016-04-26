# Generate lines from fileiter.  If whilematch is true, continue reading
# while the regexp object pat matches line.  If whilematch is false, lines
# are read so long as pat doesn't match them.  In any case, the first line
# that doesn't match pat (when whilematch is true), or that does match pat
# (when whilematch is false), is lost, and fileiter will resume at the line
# following it.
def read(fileiter, pat, whilematch):
    for line in fileiter:
        if bool(pat.match(line)) == whilematch:
            yield line
        else:
            break
