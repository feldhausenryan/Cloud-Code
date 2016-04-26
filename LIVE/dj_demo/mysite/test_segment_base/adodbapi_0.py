# -----------------  The .connect method -----------------
def connect(connection_string, timeout=30):
    """Connect to a database.
    connection_string -- An ADODB formatted connection string, see:
         * http://www.connectionstrings.com
         * http://www.asp101.com/articles/john/connstring/default.asp
    timeout -- A command timeout value, in seconds (default 30 seconds)
    """
    try:
        if not onIronPython:
            pythoncom.CoInitialize()             #v2.1 Paj
        c=Dispatch('ADODB.Connection') #connect _after_ CoIninialize v2.1.1 adamvan
    except:
        raise InterfaceError #Probably COM Error
    if verbose:
        print '%s attempting: "%s"' % (version,connection_string)
    try:
        c.CommandTimeout = timeout
        c.ConnectionString = connection_string
        c.Open()
        return Connection(c)
    except (Exception), e:
        raise OperationalError(e, "Error opening connection: " + connection_string)
