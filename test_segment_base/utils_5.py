#==============================================================================
# Date, time, timer
#==============================================================================
def localtime_to_isodate(time_struct):
    """Convert local time to ISO date"""
    s = time.strftime("%Y-%m-%d %H:%M:%S ", time_struct)
    s += "%+05d" % time.timezone
    return s
