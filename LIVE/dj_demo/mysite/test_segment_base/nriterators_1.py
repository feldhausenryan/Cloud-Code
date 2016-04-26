#
# Methods to get a given description list from another one
#
def getDescr(names, formats):
    """Create a descr description by mixing formats and names lists.
    This method assumes that names and formats descriptions structure
    are good (i.e. that checkNames and checkFormats nesterecords methods
    raised no errors).
    """
    if not names:
        names = [item for item in makeNamesFromFormats(formats)]
    if isinstance(formats, str) and isinstance(names, str):
        yield (names, formats)
        raise StopIteration
    if len(formats) != len(names):
        raise ValueError("""The formats and names structure don't match!""")
    mix = zip(names, formats)
    i = getIter(mix)
    if not i:
        return
    try:
        (name, fmt) = i.next()
        while (name, fmt):
            if isinstance(name, str) and isinstance(fmt, str):
                yield (name, fmt)
            else:
                l = []
                for (a, b) in getDescr(name[1], fmt):
                    l.append((a, b))
                yield (name[0], l)
            (name, fmt) = i.next()
    except StopIteration:
        pass
