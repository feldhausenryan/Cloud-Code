# FIXME Implement graphs with sets of values instead of lists of values
def eq(g1, g2):
    return map_values(set, g1) == map_values(set, g2)
