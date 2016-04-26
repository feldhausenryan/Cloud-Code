# Can't monkeypatch methods of anything in datetime, so we have to wrap them
def safe_fromtimestamp(timestamp, *args, **kwds):
    """ safe_fromtimestamp(timestamp) -> UTC time from POSIX timestamp.
    Timestamps outside of the valid range will be assigned datetime objects of
    Jan 1 of either MINYEAR or MAXYEAR, whichever appears closest.
    WARNING: This function does not behave properly with Daylight Savings Time,
    due to a documented issue with datetime arithmetic.
    """
    try:
        return EPOCH + timedelta(seconds=timestamp)
    except (ValueError, OverflowError), e:
        warnings.warn("Timestamp out of range.  Returning safe default value.")
        if timestamp <= 0:
            return datetime(MINYEAR, 1, 1, 0, 0, 0)
        else:
            return datetime(MAXYEAR, 1, 1, 0, 0, 0)
