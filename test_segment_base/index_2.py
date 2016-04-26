# Default filters used to compress indexes.  This is quite fast and
# compression is pretty good.
# Remember to keep these defaults in sync with the docstrings and UG.
defaultIndexFilters = Filters( complevel=1, complib='zlib',
                               shuffle=True, fletcher32=False )
