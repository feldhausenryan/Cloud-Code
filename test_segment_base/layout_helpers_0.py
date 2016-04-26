#------------------------------------------------------------------------------
# Helper Functions
#------------------------------------------------------------------------------
def expand_constraints(component, constraints):
    """ A function which expands any DeferredConstraints in the provided
    list. This is a generator function which yields the flattened stream
    of constraints.
    Paramters
    ---------
    component : Constrainable
        The constrainable component with which the constraints are
        associated. This will be passed to the .get_constraints()
        method of any DeferredConstraint instance.
    constraints : list
        The list of constraints.
    Yields
    ------
    constraints
        The stream of expanded constraints.
    """
    for cn in constraints:
        if isinstance(cn, DeferredConstraints):
            for item in cn.get_constraints(component):
                if item is not None:
                    yield item
        else:
            if cn is not None:
                yield cn
