# A list of templatizable object traits:
def TList( *args, **kw ):
    kw[ 'template' ] = 'instance'
    return List( *args, **kw )
