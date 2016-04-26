# Some functions to play with.
def foo(x, y):
    """ Foo
    Parameters
    ----------
    x : scalar : units=m
        X
    y : scalar : units=s
        Y
    Returns
    -------
    z : scalar : units=m/s
    """
    assert not isinstance(x, (UnitArray, UnitScalar))
    assert not isinstance(y, (UnitArray, UnitScalar))
    z = x / y
    return z
