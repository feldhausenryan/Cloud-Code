# wrap a python object in a COM pointer
def wrap(ob, iid=None):
    return _wrap(ob, iid, useDispatcher=(debug>0))
