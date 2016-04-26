# Useful func. to split Tcl lists and return as a dict. From Tkinter.py
def _lst2dict(lst):
    dict = {}
    for x in lst:
        dict[x[0][1:]] = (x[0][1:],) + x[1:]
    return dict
