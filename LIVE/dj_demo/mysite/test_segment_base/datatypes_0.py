#    def set_prop(self, realm, **kwargs):
#        """DataItem method proxy"""
#        self.item.set_prop(realm, **kwargs)
#
#    def __getattr__(self, name):
#        assert name in ["min_equals_max", "get_min", "get_max",
#                        "_formats","_text", "_choices", "_shape",
#                        "_format", "_label", "_xy"]
#        val = getattr(self.item, name)
#        if callable(val):
#            return bind(val, self.instance)
#        else:
#            return val
    def get_help(self):
        """Re-implement DataItem method"""
        return self.item.get_help(self.instance)
