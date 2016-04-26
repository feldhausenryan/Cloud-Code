#TODO: move this to the super class (to be created here) of EntityMeta
def process_mutators(entity):
    '''
    Apply all mutators of the given entity. That is, loop over all mutators
    in the class's mutator list and process them.
    '''
    # we don't use getattr here to not inherit from the parent mutators
    # inadvertantly if the current entity hasn't defined any mutator.
    mutators = entity.__dict__.get(MUTATORS, [])
    for mutator, args, kwargs in mutators:
        mutator.process(entity, *args, **kwargs)
