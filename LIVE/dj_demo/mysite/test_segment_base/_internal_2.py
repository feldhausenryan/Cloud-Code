# Given a datatype and an order object
#  return a new names tuple
#  with the order indicated
def _newnames(datatype, order):
    oldnames = datatype.names
    nameslist = list(oldnames)
    if isinstance(order, str):
        order = [order]
    if isinstance(order, (list, tuple)):
        for name in order:
            try:
                nameslist.remove(name)
            except ValueError:
                raise ValueError("unknown field name: %s" % (name,))
        return tuple(list(order) + nameslist)
    raise ValueError("unsupported order value: %s" % (order,))
