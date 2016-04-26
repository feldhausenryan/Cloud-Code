# Given a "public name" (eg, the name of a class, function, etc)
# make sure it is a legal (and reasonable!) Python name.
def MakePublicAttributeName(className, is_global = False):
	# Given a class attribute that needs to be public, convert it to a
	# reasonable name.
	# Also need to be careful that the munging doesnt
	# create duplicates - eg, just removing a leading "_" is likely to cause
	# a clash.
	# if is_global is True, then the name is a global variable that may
	# overwrite a builtin - eg, "None"
	if className[:2]=='__':
		return demunge_leading_underscores(className)
	elif className == 'None':
		# assign to None is evil (and SyntaxError in 2.4, even though
		# iskeyword says False there) - note that if it was a global
		# it would get picked up below
		className = 'NONE'
	elif iskeyword(className):
		# most keywords are lower case (except True, False etc in py3k)
		ret = className.capitalize()
		# but those which aren't get forced upper.
		if ret == className:
			ret = ret.upper()
		return ret
	elif is_global and hasattr(__builtins__, className):
		# builtins may be mixed case.  If capitalizing it doesn't change it,
		# force to all uppercase (eg, "None", "True" become "NONE", "TRUE"
		ret = className.capitalize()
		if ret==className: # didn't change - force all uppercase.
			ret = ret.upper()
		return ret
	# Strip non printable chars
	return ''.join([char for char in className if char in valid_identifier_chars])
