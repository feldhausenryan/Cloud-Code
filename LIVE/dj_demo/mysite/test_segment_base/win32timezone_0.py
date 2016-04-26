# for backward compatibility
def deprecated(func, name='Unknown'):
	"""This is a decorator which can be used to mark functions
	as deprecated. It will result in a warning being emmitted
	when the function is used."""
	def newFunc(*args, **kwargs):
		warnings.warn("Call to deprecated function %s." % name,
			category=DeprecationWarning)
		return func(*args, **kwargs)
	newFunc.__name__ = func.__name__
	newFunc.__doc__ = func.__doc__
	newFunc.__dict__.update(func.__dict__)
	return newFunc
