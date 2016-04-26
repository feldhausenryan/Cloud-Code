# make sure nobody creates custom nodes
def _failing_new(*args, **kwargs):
    raise TypeError('can\'t create custom node types')
