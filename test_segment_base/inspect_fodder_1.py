# line 11
def eggs(x, y):
    "A docstring."
    global fr, st
    fr = inspect.currentframe()
    st = inspect.stack()
    p = x
    q = y // 0
