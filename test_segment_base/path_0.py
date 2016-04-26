# Public functions
# ================
def checkNameValidity(name):
    """Check the validity of the `name` of an object.
    If the name is not valid, a ``ValueError`` is raised.  If it is
    valid but it can not be used with natural naming, a
    `NaturalNameWarning` is issued.
    """
    warnInfo = (
        "you will not be able to use natural naming to access this object; "
        "using ``getattr()`` will still work, though" )
    if not isinstance(name, basestring):  # Python >= 2.3
        raise TypeError("object name is not a string: %r" % (name,))
    # Check whether `name` is a valid HDF5 name.
    # http://hdfgroup.org/HDF5/doc/UG/03_Model.html#Structure
    if name == '':
        raise ValueError("the empty string is not allowed as an object name")
    if name == '.':
        raise ValueError("``.`` is not allowed as an object name")
    if '/' in name:
        raise ValueError( "the ``/`` character is not allowed "
                          "in object names: %r" % name )
    # Check whether `name` is a valid Python identifier.
    if not _pythonIdRE.match(name):
        warnings.warn( "object name is not a valid Python identifier: %r; "
                       "it does not match the pattern ``%s``; %s"
                       % (name, _pythonIdRE.pattern, warnInfo),
                       NaturalNameWarning )
        return
    # However, Python identifiers and keywords have the same form.
    if keyword.iskeyword(name):
        warnings.warn( "object name is a Python keyword: %r; %s"
                       % (name, warnInfo), NaturalNameWarning )
        return
    # Still, names starting with reserved prefixes are not allowed.
    if _reservedIdRE.match(name):
        raise ValueError( "object name starts with a reserved prefix: %r; "
                          "it matches the pattern ``%s``"
                          % (name, _reservedIdRE.pattern) )
    # ``__members__`` is the only exception to that rule.
    if name == '__members__':
        raise ValueError("``__members__`` is not allowed as an object name")
