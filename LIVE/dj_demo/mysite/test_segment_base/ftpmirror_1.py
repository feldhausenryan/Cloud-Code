# Main program: parse command line and start processing
def main():
    global verbose, interactive, mac, rmok, nologin
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'a:bil:mnp:qrs:v')
    except getopt.error, msg:
        usage(msg)
    login = ''
    passwd = ''
    account = ''
    if not args: usage('hostname missing')
    host = args[0]
    port = 0
    if ':' in host:
        host, port = host.split(':', 1)
        port = int(port)
    try:
        auth = netrc.netrc().authenticators(host)
        if auth is not None:
            login, account, passwd = auth
    except (netrc.NetrcParseError, IOError):
        pass
    for o, a in opts:
        if o == '-l': login = a
        if o == '-p': passwd = a
        if o == '-a': account = a
        if o == '-v': verbose = verbose + 1
        if o == '-q': verbose = 0
        if o == '-i': interactive = 1
        if o == '-m': mac = 1; nologin = 1; skippats.append('*.o')
        if o == '-n': nologin = 1
        if o == '-r': rmok = 1
        if o == '-s': skippats.append(a)
    remotedir = ''
    localdir = ''
    if args[1:]:
        remotedir = args[1]
        if args[2:]:
            localdir = args[2]
            if args[3:]: usage('too many arguments')
    #
    f = ftplib.FTP()
    if verbose: print "Connecting to '%s%s'..." % (host,
                                                   (port and ":%d"%port or ""))
    f.connect(host,port)
    if not nologin:
        if verbose:
            print 'Logging in as %r...' % (login or 'anonymous')
        f.login(login, passwd, account)
    if verbose: print 'OK.'
    pwd = f.pwd()
    if verbose > 1: print 'PWD =', repr(pwd)
    if remotedir:
        if verbose > 1: print 'cwd(%s)' % repr(remotedir)
        f.cwd(remotedir)
        if verbose > 1: print 'OK.'
        pwd = f.pwd()
        if verbose > 1: print 'PWD =', repr(pwd)
    #
    mirrorsubdir(f, localdir)
