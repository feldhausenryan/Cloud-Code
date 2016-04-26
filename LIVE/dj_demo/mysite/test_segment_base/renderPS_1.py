#########################################################
#
#   test code.  First, defin a bunch of drawings.
#   Routine to draw them comes at the end.
#
#########################################################
def test(outdir='epsout'):
    import os
    # print all drawings and their doc strings from the test
    # file
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    #grab all drawings from the test module
    import testshapes
    drawings = []
    for funcname in dir(testshapes):
        #if funcname[0:11] == 'getDrawing2':
        #    print 'hacked to only show drawing 2'
        if funcname[0:10] == 'getDrawing':
            drawing = eval('testshapes.' + funcname + '()')  #execute it
            docstring = eval('testshapes.' + funcname + '.__doc__')
            drawings.append((drawing, docstring))
    i = 0
    for (d, docstring) in drawings:
        filename = outdir + os.sep + 'renderPS_%d.eps'%i
        drawToFile(d,filename)
        print 'saved', filename
        i = i + 1
