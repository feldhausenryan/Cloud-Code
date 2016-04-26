#this is used to set the options from
def _setOpt(name, value, conv=None):
    '''set a module level value from environ/default'''
    from os import environ
    ename = 'RL_'+name
    if ename in environ:
        value = environ[ename]
    if conv: value = conv(value)
    globals()[name] = value
