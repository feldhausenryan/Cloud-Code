#==============================================================================
# Distribution helpers
#==============================================================================
def _remove_later(fname):
    """Try to remove file later (at exit)"""
    def try_to_remove(fname):
        if osp.exists(fname):
            os.remove(fname)
    atexit.register(try_to_remove, osp.abspath(fname))
