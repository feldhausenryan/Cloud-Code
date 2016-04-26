##		type = GL_TYPE_TO_ARRAY_MAPPING[ typeCode ]
##		for dim in dims:
##			type *= dim 
##		return type() # should expicitly set to 0s
    def arrayToGLType( self, value ):
        """Given a value, guess OpenGL type of the corresponding pointer"""
        result = ARRAY_TO_GL_TYPE_MAPPING.get( value._type_ )
        if result is not None:
            return result
        raise TypeError(
            """Don't know GL type for array of type %r, known types: %s\nvalue:%s"""%(
                value._type_, ARRAY_TO_GL_TYPE_MAPPING.keys(), value,
            )
        )
