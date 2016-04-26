##
# 30.11.2005, c
def updateDictWithVars( adict, module, pattern, group = None ):
    match = re.compile( pattern ).match
    for name in [ii for ii in vars( module ).keys()
                 if match( ii )]:
        if group is not None:
            outName = match( name ).group( group )
        else:
            outName = name
        adict[outName] = module.__dict__[name]
    return adict
