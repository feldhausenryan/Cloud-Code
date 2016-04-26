# Private functions
# =================
def same_position(oldmethod):
    """Decorate `oldmethod` to also compare the `_v_pos` attribute."""
    def newmethod(self, other):
        try:
            other._v_pos
        except AttributeError:
            return False  # not a column definition
        return self._v_pos == other._v_pos and oldmethod(self, other)
    newmethod.__name__ = oldmethod.__name__
    newmethod.__doc__ = oldmethod.__doc__
    return newmethod
