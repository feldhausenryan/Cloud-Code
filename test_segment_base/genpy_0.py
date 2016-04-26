# Given a propget function's arg desc, return the default parameters for all
# params bar the first.  Eg, then Python does a:
# object.Property = "foo"
# Python can only pass the "foo" value.  If the property has
# multiple args, and the rest have default values, this allows
# Python to correctly pass those defaults.
def MakeDefaultArgsForPropertyPut(argsDesc):
    ret = []
    for desc in argsDesc[1:]:
        default = build.MakeDefaultArgRepr(desc)
        if default is None:
            break
        ret.append(default)
    return tuple(ret)
