# *Overwrite* the existing units on an object with new units.  No unit
# conversion takes place.
def unit_array_units_overwriter(unit_array, new_units):
    """ Overwrite the units for a UnitArray with the new units.
    """
    if not hasattr(unit_array, 'units') or unit_array.units != new_units:
        unit_array.units = new_units
    return unit_array
