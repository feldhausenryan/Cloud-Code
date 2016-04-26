# Count number of leading blanks.
def getlspace(line):
    i, n = 0, len(line)
    while i < n and line[i] == " ":
        i += 1
    return i
