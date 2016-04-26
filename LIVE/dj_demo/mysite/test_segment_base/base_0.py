# Ripped from Chaco 1.0's plot_base.py
def bin_search(values, value, ascending):
    """
    Performs a binary search of a sorted array looking for a specified value.
    Returns the lowest position where the value can be found or where the
    array value is the last value less (greater) than the desired value.
    Returns -1 if *value* is beyond the minimum or maximum of *values*.
    """
    if ascending > 0:
        if (value < values[0]) or (value > values[-1]):
            return -1
    else:
        if (value < values[-1]) or (value > values[0]):
            return -1
    lo = 0
    hi = len( values )
    while True:
        mid  = (hi + lo) / 2
        test = cmp( values[ mid ], value ) * ascending
        if test == 0:
            return mid
        if test > 0:
            hi = mid
        else:
            lo = mid
        if lo >= (hi - 1):
            return lo
