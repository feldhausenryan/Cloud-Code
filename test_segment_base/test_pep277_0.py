# Destroy directory dirname and all files under it, to one level.
def deltree(dirname):
    # Don't hide legitimate errors:  if one of these suckers exists, it's
    # an error if we can't remove it.
    if os.path.exists(dirname):
        # must pass unicode to os.listdir() so we get back unicode results.
        for fname in os.listdir(unicode(dirname)):
            os.unlink(os.path.join(dirname, fname))
        os.rmdir(dirname)
