# The fixed function.
def getAttributeNames(object, includeMagic=1, includeSingle=1,
                      includeDouble=1):
    """Return list of unique attributes, including inherited, for object."""
    attributes = []
    dict = {}
    if not introspect.hasattrAlwaysReturnsTrue(object):
        # Add some attributes that don't always get picked up.
        special_attrs = ['__bases__', '__class__', '__dict__', '__name__',
                         'func_closure', 'func_code', 'func_defaults',
                         'func_dict', 'func_doc', 'func_globals', 'func_name']
        attributes += [attr for attr in special_attrs \
                       if hasattr(object, attr)]
    # For objects that have traits, get all the trait names since
    # these do not show up in dir(object).
    if hasattr(object, 'trait_names'):
        try:
            attributes += object.trait_names()
        except TypeError:
            pass
    if includeMagic:
        try: attributes += object._getAttributeNames()
        except: pass
    # Get all attribute names.
    attrdict = getAllAttributeNames(object)
    # Store the object's dir.
    object_dir = dir(object)
    for (obj_type_name, technique, count), attrlist in attrdict.items():
        # This complexity is necessary to avoid accessing all the
        # attributes of the object.  This is very handy for objects
        # whose attributes are lazily evaluated.
        if type(object).__name__ == obj_type_name and technique == 'dir':
            attributes += attrlist
        else:
            attributes += [attr for attr in attrlist \
                           if attr not in object_dir and \
                           hasattr(object, attr)]
    # Remove duplicates from the attribute list.
    for item in attributes:
        dict[item] = None
    attributes = dict.keys()
    # new-style swig wrappings can result in non-string attributes
    # e.g. ITK http://www.itk.org/
    attributes = [attribute for attribute in attributes \
                  if isinstance(attribute, basestring)]
    attributes.sort(lambda x, y: cmp(x.upper(), y.upper()))
    if not includeSingle:
        attributes = filter(lambda item: item[0]!='_' \
                            or item[1]=='_', attributes)
    if not includeDouble:
        attributes = filter(lambda item: item[:2]!='__', attributes)
    return attributes
