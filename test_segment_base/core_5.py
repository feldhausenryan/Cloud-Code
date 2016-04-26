#..........................................................
def min(obj, axis=None, out=None, fill_value=None):
    try:
        return obj.min(axis=axis, fill_value=fill_value, out=out)
    except (AttributeError, TypeError):
        # If obj doesn't have a max method,
        # ...or if the method doesn't accept a fill_value argument
        return asanyarray(obj).min(axis=axis, fill_value=fill_value, out=out)
