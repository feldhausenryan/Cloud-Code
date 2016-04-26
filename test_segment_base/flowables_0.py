#utility functions used by KeepInFrame
def _hmodel(s0,s1,h0,h1):
    # calculate the parameters in the model
    # h = a/s**2 + b/s
    a11 = 1./s0**2
    a12 = 1./s0
    a21 = 1./s1**2
    a22 = 1./s1
    det = a11*a22-a12*a21
    b11 = a22/det
    b12 = -a12/det
    b21 = -a21/det
    b22 = a11/det
    a = b11*h0+b12*h1
    b = b21*h0+b22*h1
    return a,b
