"""
import sys, time, os, cPickle, tempfile
from xml.sax.saxutils import quoteattr
try:
    from hashlib import md5
except ImportError:
    from md5 import md5

EXTENSIONS = ['.ttf','.ttc','.otf','.pfb','.pfa']

# PDF font flags (see PDF Reference Guide table 5.19)
FF_FIXED        = 1 <<  1-1
FF_SERIF        = 1 <<  2-1
FF_SYMBOLIC     = 1 <<  3-1
FF_SCRIPT       = 1 <<  4-1
FF_NONSYMBOLIC  = 1 <<  6-1
FF_ITALIC       = 1 <<  7-1
FF_ALLCAP       = 1 << 17-1
FF_SMALLCAP     = 1 << 18-1
FF_FORCEBOLD    = 1 << 19-1

class FontDescriptor:
    """This is a short descriptive record about a font.

    typeCode should be a file extension e.g. ['ttf','ttc','otf','pfb','pfa']
    """
    def __init__(self):
        self.name = None
        self.fullName = None
        self.familyName = None
        self.styleName = None
        self.isBold = False   #true if it's somehow bold
        self.isItalic = False #true if it's italic or oblique or somehow slanty
        self.isFixedPitch = False
        self.isSymbolic = False   #false for Dingbats, Symbols etc.
        self.typeCode = None   #normally the extension minus the dot
        self.fileName = None  #full path to where we found it.
        self.metricsFileName = None  #defined only for type='type1pc', or 'type1mac'
        self.timeModified = 0
