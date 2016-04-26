#    def __call__(self, ob, default=api._marker):
    def __call__(self, ob, default=_marker):
        """Adapt to this protocol"""
#        return api.adapt(ob,self,default)
        return adapt(ob,self,default)
