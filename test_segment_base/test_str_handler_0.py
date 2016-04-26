# Validation via function
def validator(object, name, value):
    if isinstance(value, basestring):
        # arbitrary rule for testing
        if value.find('fail') < 0:
            return value
        else:
            raise TraitError
    else:
        raise TraitError
