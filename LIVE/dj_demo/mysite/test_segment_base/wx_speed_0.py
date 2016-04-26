#-----------------------------------------------------------------------------
# Define a new version of DrawLines that calls the optimized
# version for numpy arrays when appropriate.
#-----------------------------------------------------------------------------
def NewDrawLines(dc,line):
    """
    """
    if (type(line) is ndarray):
        polyline(dc,line)
    else:
        dc.DrawLines(line)
