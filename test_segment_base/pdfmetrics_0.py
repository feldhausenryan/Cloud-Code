#preserve the initial values here
def _reset(
        initial_dicts = dict(
            _typefaces = _typefaces.copy(),
            _encodings = _encodings.copy(),
            _fonts = _fonts.copy(),
            )
        ):
    for k,v in initial_dicts.iteritems():
        d=globals()[k]
        d.clear()
        d.update(v)
