##def getDrawing14():
##    """This tests inherited properties.  Each font should be as it says."""
##    D = Drawing(400, 200)
##    
##    fontSize = 12
##    D.fontName = 'Courier'
##    
##    g1 = Group(
##            Rect(0, 0, 150, 20, fillColor=colors.yellow),
##            String(5, 5, 'Inherited Courier', fontName=inherit, fontSize = fontSize)
##            )
##    D.add(g1)
##
##    g2 = Group(g1, transform = translate(25,25))
##    D.add(g2)
##
##    g3 = Group(g2, transform = translate(25,25))
##    D.add(g3)
##
##    g4 = Group(g3, transform = translate(25,25))
##    D.add(g4)
##
##
##    return D
def getAllFunctionDrawingNames(doTTF=1):
    "Get a list of drawing function names from somewhere."
    funcNames = []
    # Here we get the names from the global name space.
    symbols = globals().keys()
    symbols.sort()
    for funcName in symbols:
        if funcName[0:10] == 'getDrawing':
            if doTTF or funcName!='getDrawing13':
                funcNames.append(funcName)
    return funcNames
