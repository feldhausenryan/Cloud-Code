##########################################################################
# Utility functions.
##########################################################################
def lerp(arg0,arg1,f):
    """linearly interpolate between arguments arg0 and arg1.
       The weight f is from [0..1], with f=0 giving arg0 and f=1 giving arg1"""
    return (1-f)*arg0 + f*arg1
