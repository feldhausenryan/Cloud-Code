#...............................................................................
def issequence(seq):
    """Is seq a sequence (ndarray, list or tuple)?"""
    if isinstance(seq, (ndarray, tuple, list)):
        return True
    return False
