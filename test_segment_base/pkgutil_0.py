#@simplegeneric
def iter_importer_modules(importer, prefix=''):
    if not hasattr(importer, 'iter_modules'):
        return []
    return importer.iter_modules(prefix)
