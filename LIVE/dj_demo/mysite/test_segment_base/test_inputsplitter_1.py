# Transformer tests
def transform_checker(tests, func):
    """Utility to loop over test inputs"""
    for inp, tr in tests:
        nt.assert_equals(func(inp), tr)
