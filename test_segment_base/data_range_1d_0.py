###### method to calculate bounds for a given 1-dimensional set of data
def calc_bounds(low_set, high_set, mins, maxes, epsilon, tight_bounds,
                margin=0.08, track_amount=0, bounds_func=None):
    """ Calculates bounds for a given 1-D set of data.
    Parameters
    ----------
    low_set : 'auto', 'track', or number
        Current low setting
    high_set : 'auto', 'track', or number
        Current high setting
    mins : list of numbers
        Potential minima.
    maxes : list
        Potential maxima.
    epsilon : number
        Minimum percentage difference between bounds
    tight_bounds : Boolean
        Do 'auto' bounds imply an exact fit to the data? If False, they pad a
        little bit of margin on either side.
    margin : float (default=0.08)
        The margin, expressed as a percentage of total data width, to place
        on either side of the data if tight_bounds is False.
    track_amount : number
        The amount by which a 'track' bound tracks another bound.
    bounds_func : Callable
        A callable which can override the bounds calculation.
    Returns
    -------
    (min, max) for the new bounds. If either of the calculated bounds is NaN,
    returns (0,0).
    Description
    -----------
    Setting both *low_set* and *high_set* to 'track' is an invalid state;
    the method copes by setting *high_set* to 'auto', and proceeding.
    """
    if (low_set == 'track') and (high_set == 'track'):
        high_set = 'auto'
    if low_set == 'auto':
        real_min = min(mins)
    elif low_set == 'track':
        # real_max hasn't been set yet
        pass
    else:
        real_min = low_set
    if high_set == 'auto':
        real_max = max(maxes)
    elif high_set == 'track':
        # real_min has been set now
        real_max = real_min + track_amount
    else:
        real_max = high_set
    # Go back and set real_min if we need to
    if low_set == 'track':
        real_min = real_max - track_amount
    # If we're all NaNs, just return a 0,1 range
    if isnan(real_max) or isnan(real_min):
        return 0, 0
    if not isinf(real_min) and not isinf(real_max) and \
            (abs(real_max - real_min) <= abs(epsilon * real_min)):
        # If we get here, then real_min and real_max are (for all
        # intents and purposes) identical, and so we just base
        # everything off of real_min.
        # Note: we have to use <= and not strict < because otherwise
        # we won't catch the cases when real_min == 0.0.
        if abs(real_min) > 1.0:
            # Round up to the next power of ten that encloses these
            log_val = log(abs(real_min), 10)
            if real_min >= 0:
                real_min = pow(10, floor(log_val))
                real_max = pow(10, ceil(log_val))
            else:
                real_min = -pow(10, ceil(log_val))
                real_max = -pow(10, floor(log_val))
        else:
            # If the user has a constant value less than 1, then these
            # are the bounds we use.
            if real_min > 0.0:
                real_max = 2 * real_min
                real_min = 0.0
            elif real_min == 0.0:
                real_min = -1.0
                real_max = 1.0
            else:
                real_min = 2 * real_min
                real_max = 0.0
    # Now test if the bounds leave some room around the data, unless
    # tight_bounds==True or unless another function to compute the bound
    # is provided.
    if bounds_func is not None:
        return bounds_func(real_min, real_max, margin, tight_bounds)
    elif not tight_bounds:
        low, high, d = heckbert_interval(real_min, real_max)
        # 2nd run of heckbert_interval necessary? Will be if bounds are
        # too tights (ie within the margin).
        rerun = False
        if abs(low - real_min) / (high - low) < margin:
            modified_min = real_min - (high - low) * margin
            rerun = True
        else:
            modified_min = real_min
        if abs(high - real_max) / (high - low) < margin:
            modified_max = real_max + (high - low) * margin
            rerun = True
        else:
            modified_max = real_max
        if rerun:
            low, high, d = heckbert_interval(modified_min, modified_max)
        return low, high
    else:
        return real_min, real_max
