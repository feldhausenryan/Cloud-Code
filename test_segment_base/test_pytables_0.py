# contextmanager to ensure the file cleanup
def safe_remove(path):
    if path is not None:
        import os
        try:
            os.remove(path)
        except:
            pass
