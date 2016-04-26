# This helper is needed due to a missing component in the PEP 302
# loader protocol (specifically, "get_filename" is non-standard)
# Since we can't introduce new features in maintenance releases,
# support was added to zipimporter under the name '_get_filename'
def _get_filename(loader, mod_name):
    for attr in ("get_filename", "_get_filename"):
        meth = getattr(loader, attr, None)
        if meth is not None:
            return meth(mod_name)
    return None
