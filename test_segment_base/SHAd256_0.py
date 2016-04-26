# PEP 247 module-level "new" function
def new(data=None):
    """Return a new SHAd256 hashing object"""
    if not data:
        data=b("")
    sha = _SHAd256(_SHAd256._internal, SHA256.new(data))
    sha.new = globals()['new']
    return sha
