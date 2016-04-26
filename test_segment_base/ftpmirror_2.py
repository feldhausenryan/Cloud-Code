# Core logic: mirror one subdirectory (recursively)
def mirrorsubdir(f, localdir):
    pwd = f.pwd()
    if localdir and not os.path.isdir(localdir):
        if verbose: print 'Creating local directory', repr(localdir)
        try:
            makedir(localdir)
        except os.error, msg:
            print "Failed to establish local directory", repr(localdir)
            return
    infofilename = os.path.join(localdir, '.mirrorinfo')
    try:
        text = open(infofilename, 'r').read()
    except IOError, msg:
        text = '{}'
    try:
        info = eval(text)
    except (SyntaxError, NameError):
        print 'Bad mirror info in', repr(infofilename)
        info = {}
    subdirs = []
    listing = []
    if verbose: print 'Listing remote directory %r...' % (pwd,)
    f.retrlines('LIST', listing.append)
    filesfound = []
    for line in listing:
        if verbose > 1: print '-->', repr(line)
        if mac:
            # Mac listing has just filenames;
            # trailing / means subdirectory
            filename = line.strip()
            mode = '-'
            if filename[-1:] == '/':
                filename = filename[:-1]
                mode = 'd'
            infostuff = ''
        else:
            # Parse, assuming a UNIX listing
            words = line.split(None, 8)
            if len(words) < 6:
                if verbose > 1: print 'Skipping short line'
                continue
            filename = words[-1].lstrip()
            i = filename.find(" -> ")
            if i >= 0:
                # words[0] had better start with 'l'...
                if verbose > 1:
                    print 'Found symbolic link %r' % (filename,)
                linkto = filename[i+4:]
                filename = filename[:i]
            infostuff = words[-5:-1]
            mode = words[0]
        skip = 0
        for pat in skippats:
            if fnmatch(filename, pat):
                if verbose > 1:
                    print 'Skip pattern', repr(pat),
                    print 'matches', repr(filename)
                skip = 1
                break
        if skip:
            continue
        if mode[0] == 'd':
            if verbose > 1:
                print 'Remembering subdirectory', repr(filename)
            subdirs.append(filename)
            continue
        filesfound.append(filename)
        if info.has_key(filename) and info[filename] == infostuff:
            if verbose > 1:
                print 'Already have this version of',repr(filename)
            continue
        fullname = os.path.join(localdir, filename)
        tempname = os.path.join(localdir, '@'+filename)
        if interactive:
            doit = askabout('file', filename, pwd)
            if not doit:
                if not info.has_key(filename):
                    info[filename] = 'Not retrieved'
                continue
        try:
            os.unlink(tempname)
        except os.error:
            pass
        if mode[0] == 'l':
            if verbose:
                print "Creating symlink %r -> %r" % (filename, linkto)
            try:
                os.symlink(linkto, tempname)
            except IOError, msg:
                print "Can't create %r: %s" % (tempname, msg)
                continue
        else:
            try:
                fp = open(tempname, 'wb')
            except IOError, msg:
                print "Can't create %r: %s" % (tempname, msg)
                continue
            if verbose:
                print 'Retrieving %r from %r as %r...' % (filename, pwd, fullname)
            if verbose:
                fp1 = LoggingFile(fp, 1024, sys.stdout)
            else:
                fp1 = fp
            t0 = time.time()
            try:
                f.retrbinary('RETR ' + filename,
                             fp1.write, 8*1024)
            except ftplib.error_perm, msg:
                print msg
            t1 = time.time()
            bytes = fp.tell()
            fp.close()
            if fp1 != fp:
                fp1.close()
        try:
            os.unlink(fullname)
        except os.error:
            pass            # Ignore the error
        try:
            os.rename(tempname, fullname)
        except os.error, msg:
            print "Can't rename %r to %r: %s" % (tempname, fullname, msg)
            continue
        info[filename] = infostuff
        writedict(info, infofilename)
        if verbose and mode[0] != 'l':
            dt = t1 - t0
            kbytes = bytes / 1024.0
            print int(round(kbytes)),
            print 'Kbytes in',
            print int(round(dt)),
            print 'seconds',
            if t1 > t0:
                print '(~%d Kbytes/sec)' % \
                          int(round(kbytes/dt),)
            print
    #
    # Remove files from info that are no longer remote
    deletions = 0
    for filename in info.keys():
        if filename not in filesfound:
            if verbose:
                print "Removing obsolete info entry for",
                print repr(filename), "in", repr(localdir or ".")
            del info[filename]
            deletions = deletions + 1
    if deletions:
        writedict(info, infofilename)
    #
    # Remove local files that are no longer in the remote directory
    try:
        if not localdir: names = os.listdir(os.curdir)
        else: names = os.listdir(localdir)
    except os.error:
        names = []
    for name in names:
        if name[0] == '.' or info.has_key(name) or name in subdirs:
            continue
        skip = 0
        for pat in skippats:
            if fnmatch(name, pat):
                if verbose > 1:
                    print 'Skip pattern', repr(pat),
                    print 'matches', repr(name)
                skip = 1
                break
        if skip:
            continue
        fullname = os.path.join(localdir, name)
        if not rmok:
            if verbose:
                print 'Local file', repr(fullname),
                print 'is no longer pertinent'
            continue
        if verbose: print 'Removing local file/dir', repr(fullname)
        remove(fullname)
    #
    # Recursively mirror subdirectories
    for subdir in subdirs:
        if interactive:
            doit = askabout('subdirectory', subdir, pwd)
            if not doit: continue
        if verbose: print 'Processing subdirectory', repr(subdir)
        localsubdir = os.path.join(localdir, subdir)
        pwd = f.pwd()
        if verbose > 1:
            print 'Remote directory now:', repr(pwd)
            print 'Remote cwd', repr(subdir)
        try:
            f.cwd(subdir)
        except ftplib.error_perm, msg:
            print "Can't chdir to", repr(subdir), ":", repr(msg)
        else:
            if verbose: print 'Mirroring as', repr(localsubdir)
            mirrorsubdir(f, localsubdir)
            if verbose > 1: print 'Remote cwd ..'
            f.cwd('..')
        newpwd = f.pwd()
        if newpwd != pwd:
            print 'Ended up in wrong directory after cd + cd ..'
            print 'Giving up now.'
            break
        else:
            if verbose > 1: print 'OK.'
