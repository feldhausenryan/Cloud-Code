# from reprlib 3.2.1
def recursive_repr(fillvalue=u'...'):
    u'Decorator to make a repr function return fillvalue for a recursive call'
    def decorating_function(user_function):
        repr_running = set()
        def wrapper(self):
            key = id(self), get_ident()
            if key in repr_running:
                return fillvalue
            repr_running.add(key)
            try:
                result = user_function(self)
            finally:
                repr_running.discard(key)
            return result
        # Can't use functools.wraps() here because of bootstrap issues
        wrapper.__module__ = getattr(user_function, u'__module__')
        wrapper.__doc__ = getattr(user_function, u'__doc__')
        wrapper.__name__ = getattr(user_function, u'__name__')
        wrapper.__annotations__ = getattr(user_function, u'__annotations__', {})
        return wrapper
    return decorating_function
