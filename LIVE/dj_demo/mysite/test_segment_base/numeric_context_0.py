# TODO Where should this live?
def hashable ( x ):
    try:
        hash(x)
        return True
    except TypeError:
        return False
