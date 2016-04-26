# An attribute  is defined as @attribute name value
def parse_type(attrtype):
    """Given an arff attribute value (meta data), returns its type.
    Expect the value to be a name."""
    uattribute = attrtype.lower().strip()
    if uattribute[0] == '{':
        return 'nominal'
    elif uattribute[:len('real')] == 'real':
        return 'numeric'
    elif uattribute[:len('integer')] == 'integer':
        return 'numeric'
    elif uattribute[:len('numeric')] == 'numeric':
        return 'numeric'
    elif uattribute[:len('string')] == 'string':
        return 'string'
    elif uattribute[:len('relational')] == 'relational':
        return 'relational'
    else:
        raise ParseArffError("unknown attribute %s" % uattribute)
