######################################################################
# Utility functions.
######################################################################
def is_volume_pro_available():
    """Returns `True` if there is a volume pro card available.
    """
    try:
        map = tvtk.VolumeProMapper()
    except AttributeError:
        return False
    else:
        return map.number_of_boards > 0
