# **************** WARNING! ***********************
# This function can be called during the destruction time of a table
# so measures have been taken so that it doesn't have to revive
# another node (which can fool the LRU cache). The solution devised
# has been to add a cache for autoIndex (Table._autoIndex), populate
# it in creation time of the cache (which is a safe period) and then
# update the cache whenever it changes.
# This solves the error when running test_indexes.py ManyNodesTestCase.
# F. Alted 2007-04-20
# **************************************************
def _table__getautoIndex(self):
    if self._autoIndex is None:
        try:
            indexgroup = self._v_file._getNode(_indexPathnameOf(self))
        except NoSuchNodeError:
            self._autoIndex = defaultAutoIndex  # update cache
            return self._autoIndex
        else:
            self._autoIndex = indexgroup.auto   # update cache
            return self._autoIndex
    else:
        # The value is in cache, return it
        return self._autoIndex
