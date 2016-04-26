# Templatizable object trait:
def TInstance ( *args, **kw ):
    kw[ 'template' ] = 'instance'
    return Instance( *args, **kw )
