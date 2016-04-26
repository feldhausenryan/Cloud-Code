# Helper for testing classify_class_attrs.
def attrs_wo_objs(cls):
    return [t[:3] for t in inspect.classify_class_attrs(cls)]
