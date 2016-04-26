# Join fields with optional separator
def join(words, sep = ' '):
    """join(list [,sep]) -> string
    Return a string composed of the words in list, with
    intervening occurrences of sep.  The default separator is a
    single space.
    (joinfields and join are synonymous)
    """
    return sep.join(words)
