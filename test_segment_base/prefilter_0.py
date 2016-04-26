# Handler Check Utilities
def is_shadowed(identifier, ip):
    """Is the given identifier defined in one of the namespaces which shadow
    the alias and magic namespaces?  Note that an identifier is different
    than ifun, because it can not contain a '.' character."""
    # This is much safer than calling ofind, which can change state
    return (identifier in ip.user_ns \
            or identifier in ip.user_global_ns \
            or identifier in ip.ns_table['builtin'])
