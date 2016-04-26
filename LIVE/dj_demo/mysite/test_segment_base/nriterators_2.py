# Methods to deal with descr description
def getFieldDescr(fieldName, descr):
    """Retrieve the descr list corresponding to a given field.
    For nested fields the fieldName is passed as x/y...
    This method assumes that descr description structure is good (i.e.
    that nestedrecords.checkDescr method raised no errors).
    """
    i = getIter(descr)
    if not i:
        return
    try:
        sw = ''
        item = i.next()
        while item:
            if fieldName == item[0]:
                yield item
                break
            if isinstance(item[1], list):
                if fieldName.startswith('%s/' %item[0]):
                    sw = item[0]
                else:
                    item = i.next()
                    continue
                [trash, newField] = fieldName.split(sw + '/')
                for c in getFieldDescr(newField, item[1]):
                    sw = '%s/%s' % (sw, c[0])
                    yield (sw, c[1])
            item = i.next()
    except StopIteration:
        pass
