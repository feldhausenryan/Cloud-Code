# Helper functions
def _splitparam(param):
    # Split header parameters.  BAW: this may be too simple.  It isn't
    # strictly RFC 2045 (section 5.1) compliant, but it catches most headers
    # found in the wild.  We may eventually need a full fledged parser
    # eventually.
    a, sep, b = param.partition(';')
    if not sep:
        return a.strip(), None
    return a.strip(), b.strip()
