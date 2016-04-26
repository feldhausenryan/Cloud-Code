# Get the output from a shell command into a string.
# The exit status is ignored; a trailing newline is stripped.
# Assume the command will work with '{ ... ; } 2>&1' around it..
#
def getoutput(cmd):
    """Return output (stdout or stderr) of executing cmd in a shell."""
    return getstatusoutput(cmd)[1]
