#always succeed
def add_newdoc(place, obj, doc):
    """Adds documentation to obj which is in module place.
    If doc is a string add it to obj as a docstring
    If doc is a tuple, then the first element is interpreted as
       an attribute of obj and the second as the docstring
          (method, docstring)
    If doc is a list, then each element of the list should be a
       sequence of length two --> [(method1, docstring1),
       (method2, docstring2), ...]
    This routine never raises an error.
    This routine cannot modify read-only docstrings, as appear
    in new-style classes or built-in functions. Because this
    routine never raises an error the caller must check manually
    that the docstrings were changed.
       """
    try:
        new = {}
        exec 'from %s import %s' % (place, obj) in new
        if isinstance(doc, str):
            add_docstring(new[obj], doc.strip())
        elif isinstance(doc, tuple):
            add_docstring(getattr(new[obj], doc[0]), doc[1].strip())
        elif isinstance(doc, list):
            for val in doc:
                add_docstring(getattr(new[obj], val[0]), val[1].strip())
    except:
        pass
