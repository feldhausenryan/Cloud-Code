#==============================================================================
# Updating, restoring datasets
#==============================================================================
def update_dataset(dest, source, visible_only=False):
    """
    Update `dest` dataset items from `source` dataset
    dest should inherit from DataSet, whereas source can be:
        * any Python object containing matching attribute names
        * or a dictionary with matching key names
    For each DataSet item, the function will try to get the attribute
    of the same name from the source. 
    visible_only: if True, update only visible items
    """
    for item in dest._items:
        key = item._name
        if hasattr(source, key):
            try:
                hide = item.get_prop_value("display", source, "hide", False)
            except AttributeError:
                #FIXME: Remove this try...except
                hide = False
            if visible_only and hide:
                continue
            setattr(dest, key, getattr(source, key))
        elif isinstance(source, dict) and key in source:
            setattr(dest, key, source[key])
