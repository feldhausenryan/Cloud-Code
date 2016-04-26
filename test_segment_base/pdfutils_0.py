# Read data from the JPEG file. We should probably be using PIL to
# get this information for us -- but this way is more fun!
# Returns (width, height, color components) as a triple
# This is based on Thomas Merz's code from GhostScript (viewjpeg.ps)
def readJPEGInfo(image):
    "Read width, height and number of components from open JPEG file."
    import struct
    from pdfdoc import PDFError
    #Acceptable JPEG Markers:
    #  SROF0=baseline, SOF1=extended sequential or SOF2=progressive
    validMarkers = [0xC0, 0xC1, 0xC2]
    #JPEG markers without additional parameters
    noParamMarkers = \
        [ 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7, 0xD8, 0x01 ]
    #Unsupported JPEG Markers
    unsupportedMarkers = \
        [ 0xC3, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF ]
    #read JPEG marker segments until we find SOFn marker or EOF
    done = 0
    while not done:
        x = struct.unpack('B', image.read(1))
        if x[0] == 0xFF:                    #found marker
            x = struct.unpack('B', image.read(1))
            #print "Marker: ", '%0.2x' % x[0]
            #check marker type is acceptable and process it
            if x[0] in validMarkers:
                image.seek(2, 1)            #skip segment length
                x = struct.unpack('B', image.read(1)) #data precision
                if x[0] != 8:
                    raise PDFError('JPEG must have 8 bits per component')
                y = struct.unpack('BB', image.read(2))
                height = (y[0] << 8) + y[1]
                y = struct.unpack('BB', image.read(2))
                width =  (y[0] << 8) + y[1]
                y = struct.unpack('B', image.read(1))
                color =  y[0]
                return width, height, color
            elif x[0] in unsupportedMarkers:
                raise PDFError('JPEG Unsupported JPEG marker: %0.2x' % x[0])
            elif x[0] not in noParamMarkers:
                #skip segments with parameters
                #read length and skip the data
                x = struct.unpack('BB', image.read(2))
                image.seek( (x[0] << 8) + x[1] - 2, 1)
