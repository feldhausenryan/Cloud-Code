# Capitalize the words in a string, e.g. " aBc  dEf " -> "Abc Def".
def capwords(s, sep=None):
    """capwords(s, [sep]) -> string
    Split the argument into words using split, capitalize each
    word using capitalize, and join the capitalized words using
    join. Note that this replaces runs of whitespace characters by
    a single space.
    """
    return join(map(capitalize, s.split(sep)), sep or ' ')
