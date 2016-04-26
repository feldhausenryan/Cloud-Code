# deprecated
def help(cmd=None, **opts):
    """%prog help COMMAND
    Displays help on a given command.
    """
    if cmd is None:
        raise exceptions.UsageError(None)
    try:
        func = globals()[cmd]
    except:
        raise exceptions.UsageError(
            "'%s' isn't a valid command. Try 'help COMMAND'" % cmd)
    ret = func.__doc__
    if sys.argv[0]:
        ret = ret.replace('%prog', sys.argv[0])
    return ret
