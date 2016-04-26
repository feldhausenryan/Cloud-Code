# Extracted from Text's method to serve as a function
def get_rotation(rotation):
    """
    Return the text angle as float.
    *rotation* may be 'horizontal', 'vertical', or a numeric value in degrees.
    """
    if rotation in ('horizontal', None):
        angle = 0.
    elif rotation == 'vertical':
        angle = 90.
    else:
        angle = float(rotation)
    return angle%360
