# Public functions
# ================
def check_flavor(flavor):
    """Raise a ``FlavorError`` if the `flavor` is not valid."""
    if flavor == 'numarray':
        _numarray_deprecation()
    elif flavor == 'numeric':
        _numeric_deprecation()
    if flavor not in all_flavors:
        available_flavs = ", ".join(flav for flav in all_flavors)
        raise FlavorError(
            "flavor ``%s`` is unsupported or unavailable; "
            "available flavors in this system are: %s"
            % (flavor, available_flavs) )
