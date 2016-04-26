##################################################################
#                      FUNCTION LOOKUP_TYPE                      #
##################################################################
def lookup_type(x):
    T = type(x)
    try:
        return typedefs[T]
    except:
        if isinstance(T,np.ndarray):
            return typedefs[(T,len(x.shape),x.dtype.char)]
        elif issubclass(T, InstanceType):
            return Instance(x)
        else:
            raise NotImplementedError(T)
