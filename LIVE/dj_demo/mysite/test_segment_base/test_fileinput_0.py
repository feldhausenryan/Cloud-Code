# Write lines (a list of lines) to temp file number i, and return the
# temp file's name.
def writeTmp(i, lines, mode='w'):  # opening in text mode is the default
    name = TESTFN + str(i)
    f = open(name, mode)
    f.writelines(lines)
    f.close()
    return name
