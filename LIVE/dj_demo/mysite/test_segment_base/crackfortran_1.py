####### Read fortran (77,90) code
def readfortrancode(ffile,dowithline=show,istop=1):
    """
    Read fortran codes from files and
     1) Get rid of comments, line continuations, and empty lines; lower cases.
     2) Call dowithline(line) on every line.
     3) Recursively call itself when statement \"include '<filename>'\" is met.
    """
    global gotnextfile,filepositiontext,currentfilename,sourcecodeform,strictf77,\
           beginpattern,quiet,verbose,dolowercase,include_paths
    if not istop:
        saveglobals=gotnextfile,filepositiontext,currentfilename,sourcecodeform,strictf77,\
           beginpattern,quiet,verbose,dolowercase
    if ffile==[]: return
    localdolowercase = dolowercase
    cont=0
    finalline=''
    ll=''
    commentline=re.compile(r'(?P<line>([^"]*["][^"]*["][^"!]*|[^\']*\'[^\']*\'[^\'!]*|[^!\'"]*))!{1}(?P<rest>.*)')
    includeline=re.compile(r'\s*include\s*(\'|")(?P<name>[^\'"]*)(\'|")',re.I)
    cont1=re.compile(r'(?P<line>.*)&\s*\Z')
    cont2=re.compile(r'(\s*&|)(?P<line>.*)')
    mline_mark = re.compile(r".*?'''")
    if istop: dowithline('',-1)
    ll,l1='',''
    spacedigits=[' ']+map(str,range(10))
    filepositiontext=''
    fin=fileinput.FileInput(ffile)
    while 1:
        l=fin.readline()
        if not l: break
        if fin.isfirstline():
            filepositiontext=''
            currentfilename=fin.filename()
            gotnextfile=1
            l1=l
            strictf77=0
            sourcecodeform='fix'
            ext = os.path.splitext(currentfilename)[1]
            if is_f_file(currentfilename) and \
                   not (_has_f90_header(l) or _has_fix_header(l)):
                strictf77=1
            elif is_free_format(currentfilename) and not _has_fix_header(l):
                sourcecodeform='free'
            if strictf77: beginpattern=beginpattern77
            else: beginpattern=beginpattern90
            outmess('\tReading file %s (format:%s%s)\n'\
                    %(`currentfilename`,sourcecodeform,
                      strictf77 and ',strict' or ''))
        l=l.expandtabs().replace('\xa0',' ')
        while not l=='':                       # Get rid of newline characters
            if l[-1] not in "\n\r\f": break
            l=l[:-1]
        if not strictf77:
            r=commentline.match(l)
            if r:
                l=r.group('line')+' ' # Strip comments starting with `!'
                rl=r.group('rest')
                if rl[:4].lower()=='f2py': # f2py directive
                    l = l + 4*' '
                    r=commentline.match(rl[4:])
                    if r: l=l+r.group('line')
                    else: l = l + rl[4:]
        if l.strip()=='': # Skip empty line
            cont=0
            continue
        if sourcecodeform=='fix':
            if l[0] in ['*','c','!','C','#']:
                if l[1:5].lower()=='f2py': # f2py directive
                    l='     '+l[5:]
                else: # Skip comment line
                    cont=0
                    continue
            elif strictf77:
                if len(l)>72: l=l[:72]
            if not (l[0] in spacedigits):
                raise Exception('readfortrancode: Found non-(space,digit) char '
                                'in the first column.\n\tAre you sure that '
                                'this code is in fix form?\n\tline=%s' % `l`)
            if (not cont or strictf77) and (len(l)>5 and not l[5]==' '):
                # Continuation of a previous line
                ll=ll+l[6:]
                finalline=''
                origfinalline=''
            else:
                if not strictf77:
                    # F90 continuation
                    r=cont1.match(l)
                    if r: l=r.group('line') # Continuation follows ..
                    if cont:
                        ll=ll+cont2.match(l).group('line')
                        finalline=''
                        origfinalline=''
                    else:
                        l='     '+l[5:] # clean up line beginning from possible digits.
                        if localdolowercase: finalline=ll.lower()
                        else: finalline=ll
                        origfinalline=ll
                        ll=l
                    cont=(r is not None)
                else:
                    l='     '+l[5:] # clean up line beginning from possible digits.
                    if localdolowercase: finalline=ll.lower()
                    else: finalline=ll
                    origfinalline =ll
                    ll=l
        elif sourcecodeform=='free':
            if not cont and ext=='.pyf' and mline_mark.match(l):
                l = l + '\n'
                while 1:
                    lc = fin.readline()
                    if not lc:
                        errmess('Unexpected end of file when reading multiline\n')
                        break
                    l = l + lc
                    if mline_mark.match(lc):
                        break
                l = l.rstrip()
            r=cont1.match(l)
            if r: l=r.group('line') # Continuation follows ..
            if cont:
                ll=ll+cont2.match(l).group('line')
                finalline=''
                origfinalline=''
            else:
                if localdolowercase: finalline=ll.lower()
                else: finalline=ll
                origfinalline =ll
                ll=l
            cont=(r is not None)
        else:
            raise ValueError("Flag sourcecodeform must be either 'fix' or 'free': %s"%`sourcecodeform`)
        filepositiontext='Line #%d in %s:"%s"\n\t' % (fin.filelineno()-1,currentfilename,l1)
        m=includeline.match(origfinalline)
        if m:
            fn=m.group('name')
            if os.path.isfile(fn):
                readfortrancode(fn,dowithline=dowithline,istop=0)
            else:
                include_dirs = [os.path.dirname(currentfilename)] + include_paths
                foundfile = 0
                for inc_dir in include_dirs:
                    fn1 = os.path.join(inc_dir,fn)
                    if os.path.isfile(fn1):
                        foundfile = 1
                        readfortrancode(fn1,dowithline=dowithline,istop=0)
                        break
                if not foundfile:
                    outmess('readfortrancode: could not find include file %s in %s. Ignoring.\n'%(`fn`, os.pathsep.join(include_dirs)))
        else:
            dowithline(finalline)
        l1=ll
    if localdolowercase:
        finalline=ll.lower()
    else: finalline=ll
    origfinalline = ll
    filepositiontext='Line #%d in %s:"%s"\n\t' % (fin.filelineno()-1,currentfilename,l1)
    m=includeline.match(origfinalline)
    if m:
        fn=m.group('name')
        if os.path.isfile(fn):
            readfortrancode(fn,dowithline=dowithline,istop=0)
        else:
            include_dirs = [os.path.dirname(currentfilename)] + include_paths
            foundfile = 0
            for inc_dir in include_dirs:
                fn1 = os.path.join(inc_dir,fn)
                if os.path.isfile(fn1):
                    foundfile = 1
                    readfortrancode(fn1,dowithline=dowithline,istop=0)
                    break
            if not foundfile:
                outmess('readfortrancode: could not find include file %s in %s. Ignoring.\n'%(`fn`, os.pathsep.join(include_dirs)))
    else:
        dowithline(finalline)
    filepositiontext=''
    fin.close()
    if istop: dowithline('',1)
    else:
        gotnextfile,filepositiontext,currentfilename,sourcecodeform,strictf77,\
           beginpattern,quiet,verbose,dolowercase=saveglobals
