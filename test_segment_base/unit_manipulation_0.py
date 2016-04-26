# Convert objects with units to the same type of object with new units.
def unit_array_units_converter(unit_array, new_units):
    """ Convert a UnitArray from one set of units to another.
    """
    if unit_array.units != new_units:
        # Need conversion.
        if isinstance(unit_array, ndarray) and unit_array.shape != ():
            # this is an array
            result = UnitArray(units.convert(unit_array.view(ndarray), unit_array.units,
                                   new_units))
        else:
            # this is a scalar
            result = UnitScalar(units.convert(unit_array.view(ndarray), unit_array.units,
                                   new_units))
        result.units = new_units
    else:
        # No conversion needed.  Just return the unit_array.
        result = unit_array
    return result
