# To convert typecharacters we need to
# Not very safe.  Disabled for now..
def replacetypechars(astr):
    astr = astr.replace("'s'","'h'")
    astr = astr.replace("'b'","'B'")
    astr = astr.replace("'1'","'b'")
    astr = astr.replace("'w'","'H'")
    astr = astr.replace("'u'","'I'")
    return astr
