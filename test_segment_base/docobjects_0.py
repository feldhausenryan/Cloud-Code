""" % (indent_str, self.name, self.file, indent_str, indented_docstring)

class Function(DocObject):
    """ documentable function """
    def __init__(self, name, file, lineno, argnames, defaults, parent_module,
                 varargs=0, kwargs=0, docstring = "", children = [ ]):
        DocObject.__init__(self, name, parent_module.abs_name + '.' + name,
                           file, lineno, parent_module, docstring, children)
        self.argnames = argnames
        self.defaults = defaults
        self.varargs = varargs
        self.kwargs = kwargs
        # qualifications to function (e.g. 'staticmethod')
        self.qualifications = [ ]
