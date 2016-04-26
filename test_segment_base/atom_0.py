# Private functions
# =================
def _invalid_itemsize_error(kind, itemsize, itemsizes):
    isizes = sorted(itemsizes)
    return ValueError( "invalid item size for kind ``%s``: %r; "
                       "it must be one of ``%r``"
                       % (kind, itemsize, isizes) )
