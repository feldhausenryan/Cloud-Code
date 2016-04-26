#-----------------------------------------------------------------------------
# Local utilities
#-----------------------------------------------------------------------------
def sleeper(interval=t_short, *a, **kw):
    args = dict(interval=interval,
                other_args=a,
                kw_args=kw)
    time.sleep(interval)
    return args
