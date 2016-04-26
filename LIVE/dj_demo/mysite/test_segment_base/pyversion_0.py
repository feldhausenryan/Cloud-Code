# To be forward-compatible, we do all list sorts using keys instead of cmp
# functions.  However, part of the unittest.TestLoader API involves a
# user-provideable cmp function, so we need some way to convert that.
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class Key(object):
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
    return Key
