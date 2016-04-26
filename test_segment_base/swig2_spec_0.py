"""

class swig2_converter(common_base_converter):
    """ A converter for SWIG >= 1.3 wrapped objects."""
    def __init__(self, class_name="undefined", pycobj=0, runtime_version=None):
        """Initializes the instance.
        Parameters
        ----------
        - class_name : `string`
          Name of class, this is set dynamically at build time by the
          `type_spec` method.
        - pycobj : `int`
          If `pycobj` is 0 then code is generated to deal with string
          representations of the SWIG wrapped pointer.  If it is 1,
          then code is generated to deal with a PyCObject.  If it is 2
          then code is generated to deal with with PySwigObject.
        - runtime_version : `int`
          Specifies the SWIG_RUNTIME_VERSION to use.  Defaults to
          `None`.  In this case the runtime is automatically
          determined.  This option is useful if you want to force the
          runtime_version to be a specific one and override the
          auto-detected one.
        """
        self.class_name = class_name
        self.pycobj = pycobj # This is on if a PyCObject has been used.
        self.runtime_version = runtime_version
        common_base_converter.__init__(self)
