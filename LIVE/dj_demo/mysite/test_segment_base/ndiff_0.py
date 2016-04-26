# open a file & return the file object; gripe and return 0 if it
# couldn't be opened
def fopen(fname):
    try:
        return open(fname, 'U')
    except IOError, detail:
        return fail("couldn't open " + fname + ": " + str(detail))
