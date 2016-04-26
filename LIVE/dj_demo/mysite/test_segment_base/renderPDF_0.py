#########################################################
#
#   test code.  First, define a bunch of drawings.
#   Routine to draw them comes at the end.
#
#########################################################
def test():
    from reportlab.graphics.shapes import _baseGFontName, _baseGFontNameBI
    c = Canvas('renderPDF.pdf')
    c.setFont(_baseGFontName, 36)
    c.drawString(80, 750, 'Graphics Test')
    # print all drawings and their doc strings from the test
    # file
    #grab all drawings from the test module
    from reportlab.graphics import testshapes
    drawings = []
    for funcname in dir(testshapes):
        if funcname[0:10] == 'getDrawing':
            drawing = eval('testshapes.' + funcname + '()')  #execute it
            docstring = eval('testshapes.' + funcname + '.__doc__')
            drawings.append((drawing, docstring))
    #print in a loop, with their doc strings
    c.setFont(_baseGFontName, 12)
    y = 740
    i = 1
    for (drawing, docstring) in drawings:
        assert (docstring is not None), "Drawing %d has no docstring!" % i
        if y < 300:  #allows 5-6 lines of text
            c.showPage()
            y = 740
        # draw a title
        y = y - 30
        c.setFont(_baseGFontNameBI,12)
        c.drawString(80, y, 'Drawing %d' % i)
        c.setFont(_baseGFontName,12)
        y = y - 14
        textObj = c.beginText(80, y)
        textObj.textLines(docstring)
        c.drawText(textObj)
        y = textObj.getY()
        y = y - drawing.height
        draw(drawing, c, 80, y)
        i = i + 1
    if y!=740: c.showPage()
    c.save()
    print 'saved renderPDF.pdf'
