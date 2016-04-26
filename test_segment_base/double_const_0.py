# Verify that the double x is within a few bits of eval(x_str).
def check_ok(x, x_str):
    assert x > 0.0
    x2 = eval(x_str)
    assert x2 > 0.0
    diff = abs(x - x2)
    # If diff is no larger than 3 ULP (wrt x2), then diff/8 is no larger
    # than 0.375 ULP, so adding diff/8 to x2 should have no effect.
    if x2 + (diff / 8.) != x2:
        raise TestFailed("Manifest const %s lost too much precision " % x_str)
