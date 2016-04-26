# does if 0: dummy(x) get us x into the scope?
def unoptimize_before_dead_code():
    x = 42
    def f():
        if 0: dummy(x)
    return f
