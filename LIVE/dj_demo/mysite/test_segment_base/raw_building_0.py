# TODO : find a nicer way to handle this situation;
# However __proxied introduced an
# infinite recursion (see https://bugs.launchpad.net/pylint/+bug/456870)
def _set_proxied(const):
    return _CONST_PROXY[const.value.__class__]
