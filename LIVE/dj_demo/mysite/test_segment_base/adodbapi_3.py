# # # # #
def _convert_to_python(variant, function): # convert DB value into Python value
    if isinstance(variant,DBNull):
        return None
    return function(variant)
