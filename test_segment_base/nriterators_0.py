#
# Methods for flatten the buffer structure descriptions
#
def flattenDescr(descr, check=False):
    """Flatten a descr description of a buffer.
    Names of nested fields are returned as a level1/level2/.../levelN path.
    If ``check`` is True the function returns None when it finds some element
    with an incorrect format. This is not strictely necessary, but it is
    useful for testing purposes.
    """
    i = getIter(descr)
    if not i:
        return
    try:
        item = i.next()
        while item:
            if isinstance(item, tuple) and len(item) == 2 and \
            (isinstance(item[1], str) or isinstance(item[1], list)) and \
            isinstance(item[0], str):
                if isinstance(item[1], str):
                    yield item
                else:
                    for c in flattenDescr(item[1], check):
                        if c == None:
                            yield c
                        else:
                            name = '%s/%s' % (item[0], c[0])
                            yield (name, c[1])
            else:
                if check:
                    yield None
            item = i.next()
    except StopIteration:
        pass
