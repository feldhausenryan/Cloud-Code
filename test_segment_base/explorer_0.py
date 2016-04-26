# Factory function for exploring a Python namespace.
def explore(obj):
    """ View a Python object as a naming context. """
    root = Binding(name='root', obj=PyContext(namespace=obj))
    explorer = Explorer(root=root, size=(1200, 400))
    explorer.open()
    return
