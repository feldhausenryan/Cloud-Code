"""

from reportlab.platypus.flowables import *
from reportlab.lib.units import inch
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.frames import Frame
from reportlab.rl_config import defaultPageSize, verbose
import reportlab.lib.sequencer
from reportlab.pdfgen import canvas
try:
    set
except NameError:
    from sets import Set as set

from base64 import encodestring, decodestring
try:
    import cPickle as pickle
except ImportError:
    import pickle
dumps = pickle.dumps
loads = pickle.loads

from types import *
import sys
import logging
logger = logging.getLogger("reportlab.platypus")

class LayoutError(Exception):
    pass

def _fSizeString(f):
    #used to get size during error messages
    w=getattr(f,'width',None)
    if w is None:
        w=getattr(f,'_width',None)

    h=getattr(f,'height',None)
    if h is None:
        h=getattr(f,'_height',None)
    #tables in particular may have some nasty large culprit
    if hasattr(f, '_culprit'):
        c = ', %s, ' % f._culprit()
    else:
        c = ''
    if w is not None or h is not None:
        if w is None: w='???'
        if h is None: h='???'
        return '(%s x %s)%s' % (w,h,c)
    return ''

def _doNothing(canvas, doc):
    "Dummy callback for onPage"
    pass

class PTCycle(list):
    def __init__(self):
        self._restart = 0
        self._idx = 0
        list.__init__(self)

    def cyclicIterator(self):
        while 1:
            yield self[self._idx]
            self._idx += 1
            if self._idx>=len(self):
                self._idx = self._restart

class IndexingFlowable(Flowable):
    """Abstract interface definition for flowables which might
    hold references to other pages or themselves be targets
    of cross-references.  XRefStart, XRefDest, Table of Contents,
    Indexes etc."""
    def isIndexing(self):
        return 1
