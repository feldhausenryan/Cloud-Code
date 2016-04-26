# Store "item" in "dict" under "key".
# The dictionary maps keys to lists of items.
# If there is no list for the key yet, it is created.
#
def store(dict, key, item):
    if dict.has_key(key):
        dict[key].append(item)
    else:
        dict[key] = [item]
