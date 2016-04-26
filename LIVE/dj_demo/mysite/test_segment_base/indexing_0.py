# the supported indexers
def get_indexers_list():
    return [
        ('ix'  ,_NDFrameIndexer),
        ('iloc',_iLocIndexer   ),
        ('loc' ,_LocIndexer    ),
        ('at'  ,_AtIndexer     ),
        ('iat' ,_iAtIndexer    ),
        ]
