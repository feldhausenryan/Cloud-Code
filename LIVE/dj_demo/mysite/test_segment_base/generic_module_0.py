################################################################################
# Utility function.
################################################################################
def find_object_given_state(needle, haystack, object):
    """
    Find the object which corrsponds to given state instance (`needle`)
    in the given state (`haystack`) and object representing that
    haystack.
    Parameters
    ----------
    `needle` -- The `State` instance to find
    haystack -- The source State in which we are to find the state
    `object` -- the object corresponding to the `haystack`
    """
    if needle is haystack:
        return object
    if hasattr(object, 'filter'):
        return find_object_given_state(needle,
                                       haystack.filter,
                                       object.filter)
    elif hasattr(object, 'filters'):
        for h, obj in zip(haystack.filters, object.filters):
            r = find_object_given_state(needle, h, obj)
            if r is not None:
                return r
    return None
