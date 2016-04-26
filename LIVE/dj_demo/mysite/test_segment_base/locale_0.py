# Iterate over grouping intervals
def _grouping_intervals(grouping):
    last_interval = None
    for interval in grouping:
        # if grouping is -1, we are done
        if interval == CHAR_MAX:
            return
        # 0: re-use last group ad infinitum
        if interval == 0:
            if last_interval is None:
                raise ValueError("invalid grouping")
            while True:
                yield last_interval
        yield interval
        last_interval = interval
