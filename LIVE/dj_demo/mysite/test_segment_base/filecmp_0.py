# Compare two files.
# Return:
#       0 for equal
#       1 for different
#       2 for funny cases (can't stat, etc.)
#
def _cmp(a, b, sh, abs=abs, cmp=cmp):
    try:
        return not abs(cmp(a, b, sh))
    except (os.error, IOError):
        return 2
