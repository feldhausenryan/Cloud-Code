# Factory function for creating bindings.
def bind_preference(obj, trait_name, preference_path, preferences=None):
    """ Create a new preference binding. """
    # This may seem a bit wierd, but we manually build up a dictionary of
    # the traits that need to be set at the time the 'PreferenceBinding'
    # instance is created.
    #
    # This is because we only want to set the 'preferences' trait iff one
    # is explicitly specified. If we passed it in with the default argument
    # value of 'None' then it counts as 'setting' the trait which prevents
    # the binding instance from defaulting to the package-global preferences.
    # Also, if we try to set the 'preferences' trait *after* construction time
    # then it is too late as the binding initialization is done in the
    # constructor (we could of course split that out, which may be the 'right'
    # way to do it ;^).
    traits = {
        'obj'             : obj,
        'trait_name'      : trait_name,
        'preference_path' : preference_path
    }
    if preferences is not None:
        traits['preferences'] = preferences
    return PreferenceBinding(**traits)
