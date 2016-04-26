# TODO: move this to cp.log.log_type_converters
def convert_log_index(log_index, unit_system=None, to_unit=None, family_name=None):
    """ Function to convert the units of a LogIndex
        Parameters
        ----------
        log_index
            index to be converted
        unit_system
            the unit system of the current log_index units, defaults to the
            unit_managers default system (current unit_system):
        to_units
            new_units to convert to
        family_name
            provided in cases where the family_name attribute is not present
            in the provided log_index object
        """
    if family_name==None:
        family_name=log_index.family_name or log_index.name
    if to_unit==None:
        unit_system = _get_unit_system(unit_system)
        try:
            to_unit = unit_system.units(family_name)
        except KeyError:
            logger.exception("Could not convert LogIndex: %s to system: %s" % \
                              (log_index, unit_system))
            return log_index.clone()
    if log_index.units == to_unit:
        new_log_index = log_index.clone()
        new_log_index.family_name = family_name # TODO: not sure if I need this
    else:
