# line 1
def wrap(foo=None):
    def wrapper(func):
        return func
    return wrapper
