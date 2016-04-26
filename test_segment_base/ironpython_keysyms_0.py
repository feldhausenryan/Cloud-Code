# function to handle the mapping
def make_keysym(keycode):
    try:
        sym = code2sym_map[keycode]
    except KeyError:
        sym = ''
    return sym
