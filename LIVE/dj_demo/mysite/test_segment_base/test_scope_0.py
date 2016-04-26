""")

        check_syntax_error(self, """\
def unoptimized_clash2():
    from string import *
    def f(s):
        return strip(s) # ambiguity: global or local
    return f
""")

        check_syntax_error(self, """\
def unoptimized_clash2():
    from string import *
    def g():
        def f(s):
            return strip(s) # ambiguity: global or local
        return f
""")

        # XXX could allow this for exec with const argument, but what's the point
        check_syntax_error(self, """\
def error(y):
    exec "a = 1"
    def f(x):
        return x + y
    return f
""")

        check_syntax_error(self, """\
def f(x):
    def g():
        return x
    del x # can't del name
""")

        check_syntax_error(self, """\
def f():
    def g():
        from string import *
        return strip # global or local?
""")

        # and verify a few cases that should work

        exec """
def noproblem1():
    from string import *
    f = lambda x:x
