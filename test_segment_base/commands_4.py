# Make a shell command argument from a string.
# Return a string beginning with a space followed by a shell-quoted
# version of the argument.
# Two strategies: enclose in single quotes if it contains none;
# otherwise, enclose in double quotes and prefix quotable characters
# with backslash.
#
def mkarg(x):
    if '\'' not in x:
        return ' \'' + x + '\''
    s = ' "'
    for c in x:
        if c in '\\$"`':
            s = s + '\\'
        s = s + c
    s = s + '"'
    return s
