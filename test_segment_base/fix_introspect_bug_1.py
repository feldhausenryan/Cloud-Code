# This is also a modified version of the function which does not use
# str(object).
def getAllAttributeNames(object):
    """Return dict of all attributes, including inherited, for an object.
    Recursively walk through a class and all base classes.
    """
    attrdict = {}  # (object, technique, count): [list of attributes]
    # !!!
    # Do Not use hasattr() as a test anywhere in this function,
    # because it is unreliable with remote objects: xmlrpc, soap, etc.
    # They always return true for hasattr().
    # !!!
    try:
        # This could(?) fail if the type is poorly defined without
        # even a name.
        key = type(object).__name__
    except:
        key = 'anonymous'
    # Wake up sleepy objects - a hack for ZODB objects in "ghost" state.
    wakeupcall = dir(object)
    del wakeupcall
    # Get attributes available through the normal convention.
    attributes = dir(object)
    attrdict[(key, 'dir', len(attributes))] = attributes
    # Get attributes from the object's dictionary, if it has one.
    try:
        attributes = object.__dict__.keys()
        attributes.sort()
    except:  # Must catch all because object might have __getattr__.
        pass
    else:
        attrdict[(key, '__dict__', len(attributes))] = attributes
    # For a class instance, get the attributes for the class.
    try:
        klass = object.__class__
    except:  # Must catch all because object might have __getattr__.
        pass
    else:
        if klass is object:
            # Break a circular reference. This happens with extension
            # classes.
            pass
        else:
            attrdict.update(getAllAttributeNames(klass))
    # Also get attributes from any and all parent classes.
    try:
        bases = object.__bases__
    except:  # Must catch all because object might have __getattr__.
        pass
    else:
        if isinstance(bases, types.TupleType):
            for base in bases:
                if type(base) is types.TypeType:
                    # Break a circular reference. Happens in Python 2.2.
                    pass
                else:
                    attrdict.update(getAllAttributeNames(base))
    return attrdict
