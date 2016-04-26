#
# Methods to deal with the names description
#
def getSubNames(names):
    """Retrieve the list of all names and sub-names in a names list.
    For nested fields all sub-field names are returned. For instance,
    a field x/y/z will be returned as x, y, z.
    This method is used to check that field names don't contain
    '/' characters.
    This method assumes that names description structure is good (i.e.
    that nestedrecords.checkNames method raised no errors).
    """
    i = getIter(names)
    if not i:
        return
    try:
        item = i.next()
        while item:
            if isinstance(item, str):
                yield item
            else:
