# Note that we don't use inspect.getmembers because of
# http://bugs.python.org/issue1785
# See also http://elixir.ematia.de/trac/changeset/262
def getmembers(object, predicate=None):
    base_props = []
    for key in dir(object):
        try:
            value = getattr(object, key)
        except AttributeError:
            continue
        if not predicate or predicate(value):
            base_props.append((key, value))
    return base_props
