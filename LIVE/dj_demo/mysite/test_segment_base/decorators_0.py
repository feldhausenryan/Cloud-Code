# Simple example of the basic idea
def as_unittest(func):
    """Decorator to make a simple function into a normal test via unittest."""
    class Tester(unittest.TestCase):
        def test(self):
            func()
    Tester.__name__ = func.__name__
    return Tester
