# -----------------------------------------------------------------------------
# lex(module)
#
# Build all of the regular expression rules from definitions in the supplied module
# -----------------------------------------------------------------------------
def lex(module=None,object=None,debug=0,optimize=0,lextab="lextab",reflags=0,nowarn=0,outputdir="", debuglog=None, errorlog=None):
    global lexer
    ldict = None
    stateinfo  = { 'INITIAL' : 'inclusive'}
    lexobj = Lexer()
    lexobj.lexoptimize = optimize
    global token,input
    if errorlog is None:
        errorlog = PlyLogger(sys.stderr)
    if debug:
        if debuglog is None:
            debuglog = PlyLogger(sys.stderr)
    # Get the module dictionary used for the lexer
    if object: module = object
    if module:
        _items = [(k,getattr(module,k)) for k in dir(module)]
        ldict = dict(_items)
    else:
        ldict = get_caller_module_dict(2)
    # Collect parser information from the dictionary
    linfo = LexerReflect(ldict,log=errorlog,reflags=reflags)
    linfo.get_all()
    if not optimize:
        if linfo.validate_all():
            raise SyntaxError("Can't build lexer")
    if optimize and lextab:
        try:
            lexobj.readtab(lextab,ldict)
            token = lexobj.token
            input = lexobj.input
            lexer = lexobj
            return lexobj
        except ImportError:
            pass
    # Dump some basic debugging information
    if debug:
        debuglog.info("lex: tokens   = %r", linfo.tokens)
        debuglog.info("lex: literals = %r", linfo.literals)
        debuglog.info("lex: states   = %r", linfo.stateinfo)
    # Build a dictionary of valid token names
    lexobj.lextokens = { }
    for n in linfo.tokens:
        lexobj.lextokens[n] = 1
    # Get literals specification
    if isinstance(linfo.literals,(list,tuple)):
        lexobj.lexliterals = type(linfo.literals[0])().join(linfo.literals)
    else:
        lexobj.lexliterals = linfo.literals
    # Get the stateinfo dictionary
    stateinfo = linfo.stateinfo
    regexs = { }
    # Build the master regular expressions
    for state in stateinfo:
        regex_list = []
        # Add rules defined by functions first
        for fname, f in linfo.funcsym[state]:
            line = func_code(f).co_firstlineno
            file = func_code(f).co_filename
            regex_list.append("(?P<%s>%s)" % (fname,f.__doc__))
            if debug:
                debuglog.info("lex: Adding rule %s -> '%s' (state '%s')",fname,f.__doc__, state)
        # Now add all of the simple rules
        for name,r in linfo.strsym[state]:
            regex_list.append("(?P<%s>%s)" % (name,r))
            if debug:
                debuglog.info("lex: Adding rule %s -> '%s' (state '%s')",name,r, state)
        regexs[state] = regex_list
    # Build the master regular expressions
    if debug:
        debuglog.info("lex: ==== MASTER REGEXS FOLLOW ====")
    for state in regexs:
        lexre, re_text, re_names = _form_master_re(regexs[state],reflags,ldict,linfo.toknames)
        lexobj.lexstatere[state] = lexre
        lexobj.lexstateretext[state] = re_text
        lexobj.lexstaterenames[state] = re_names
        if debug:
            for i in range(len(re_text)):
                debuglog.info("lex: state '%s' : regex[%d] = '%s'",state, i, re_text[i])
    # For inclusive states, we need to add the regular expressions from the INITIAL state
    for state,stype in stateinfo.items():
        if state != "INITIAL" and stype == 'inclusive':
             lexobj.lexstatere[state].extend(lexobj.lexstatere['INITIAL'])
             lexobj.lexstateretext[state].extend(lexobj.lexstateretext['INITIAL'])
             lexobj.lexstaterenames[state].extend(lexobj.lexstaterenames['INITIAL'])
    lexobj.lexstateinfo = stateinfo
    lexobj.lexre = lexobj.lexstatere["INITIAL"]
    lexobj.lexretext = lexobj.lexstateretext["INITIAL"]
    lexobj.lexreflags = reflags
    # Set up ignore variables
    lexobj.lexstateignore = linfo.ignore
    lexobj.lexignore = lexobj.lexstateignore.get("INITIAL","")
    # Set up error functions
    lexobj.lexstateerrorf = linfo.errorf
    lexobj.lexerrorf = linfo.errorf.get("INITIAL",None)
    if not lexobj.lexerrorf:
        errorlog.warning("No t_error rule is defined")
    # Check state information for ignore and error rules
    for s,stype in stateinfo.items():
        if stype == 'exclusive':
              if not s in linfo.errorf:
                   errorlog.warning("No error rule is defined for exclusive state '%s'", s)
              if not s in linfo.ignore and lexobj.lexignore:
                   errorlog.warning("No ignore rule is defined for exclusive state '%s'", s)
        elif stype == 'inclusive':
              if not s in linfo.errorf:
                   linfo.errorf[s] = linfo.errorf.get("INITIAL",None)
              if not s in linfo.ignore:
                   linfo.ignore[s] = linfo.ignore.get("INITIAL","")
    # Create global versions of the token() and input() functions
    token = lexobj.token
    input = lexobj.input
    lexer = lexobj
    # If in optimize mode, we write the lextab
    if lextab and optimize:
        lexobj.writetab(lextab,outputdir)
    return lexobj
