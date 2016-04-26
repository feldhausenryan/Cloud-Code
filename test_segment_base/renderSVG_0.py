### helper functions ###
def _pointsFromList(L):
    """
    given a list of coordinates [x0, y0, x1, y1....]
    produce a list of points [(x0,y0), (y1,y0),....]
    """
    P=[]
    for i in range(0,len(L), 2):
        P.append((L[i], L[i+1]))
    return P
