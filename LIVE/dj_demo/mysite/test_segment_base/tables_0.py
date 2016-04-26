"""
from reportlab.platypus.flowables import Flowable, Preformatted, Spacer
from reportlab import rl_config
from reportlab.lib.styles import PropertySet, ParagraphStyle, _baseFontName
from reportlab.lib import colors
from reportlab.lib.utils import fp_str, annotateException, IdentStr, flatten
from reportlab.lib.abag import ABag as CellFrame
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus.doctemplate import Indenter
from reportlab.platypus.flowables import LIIndenter

LINECAPS={None: None, 'butt':0,'round':1,'projecting':2,'squared':2}
LINEJOINS={None: None, 'miter':0, 'mitre':0, 'round':1,'bevel':2}

class CellStyle(PropertySet):
    fontname = _baseFontName
    fontsize = 10
    leading = 12
    leftPadding = 6
    rightPadding = 6
    topPadding = 3
    bottomPadding = 3
    firstLineIndent = 0
    color = 'black'
    alignment = 'LEFT'
    background = 'white'
    valign = "BOTTOM"
    href = None
    destination = None
    def __init__(self, name, parent=None):
        self.name = name
        if parent is not None:
            parent.copy(self)
    def copy(self, result=None):
        if result is None:
            result = CellStyle()
        for name in dir(self):
            setattr(result, name, getattr(self, name))
        return result

class TableStyle:
    def __init__(self, cmds=None, parent=None, **kw):
        #handle inheritance from parent first.
        commands = []
        if parent:
            # copy the parents list at construction time
            commands = commands + parent.getCommands()
            self._opts = parent._opts
            for a in ('spaceBefore','spaceAfter'):
                if hasattr(parent,a):
                    setattr(self,a,getattr(parent,a))
        if cmds:
            commands = commands + list(cmds)
        self._cmds = commands
        self._opts={}
        self._opts.update(kw)

    def add(self, *cmd):
        self._cmds.append(cmd)
    def __repr__(self):
        return "TableStyle(\n%s\n) # end TableStyle" % "  \n".join(map(repr, self._cmds))
    def getCommands(self):
        return self._cmds

def _rowLen(x):
    return not isinstance(x,(tuple,list)) and 1 or len(x)

def _calc_pc(V,avail):
    '''check list V for percentage or * values
    1) absolute values go through unchanged
    2) percentages are used as weights for unconsumed space
    3) if no None values were seen '*' weights are
    set equally with unclaimed space
    otherwise * weights are assigned as None'''
    R = []
    r = R.append
    I = []
    i = I.append
    J = []
    j = J.append
    s = avail
    w = n = 0.
    for v in V:
        if isinstance(v,basestring):
            v = v.strip()
            if not v:
                v = None
                n += 1
            elif v.endswith('%'):
                v = float(v[:-1])
                w += v
                i(len(R))
            elif v=='*':
                j(len(R))
            else:
                v = float(v)
                s -= v
        elif v is None:
            n += 1
        else:
            s -= v
        r(v)
    s = max(0.,s)
    f = s/max(100.,w)
    for i in I:
        R[i] *= f
        s -= R[i]
    s = max(0.,s)
    m = len(J)
    if m:
        v =  n==0 and s/m or None
        for j in J:
            R[j] = v
    return R

def _hLine(canvLine, scp, ecp, y, hBlocks, FUZZ=rl_config._FUZZ):
    '''
    Draw horizontal lines; do not draw through regions specified in hBlocks
    This also serves for vertical lines with a suitable canvLine
    '''
    if hBlocks: hBlocks = hBlocks.get(y,None)
    if not hBlocks or scp>=hBlocks[-1][1]-FUZZ or ecp<=hBlocks[0][0]+FUZZ:
        canvLine(scp,y,ecp,y)
    else:
        i = 0
        n = len(hBlocks)
        while scp<ecp-FUZZ and i<n:
            x0, x1 = hBlocks[i]
            if x1<=scp+FUZZ or x0>=ecp-FUZZ:
                i += 1
                continue
            i0 = max(scp,x0)
            i1 = min(ecp,x1)
            if i0>scp: canvLine(scp,y,i0,y)
            scp = i1
        if scp<ecp-FUZZ: canvLine(scp,y,ecp,y)

def _multiLine(scp,ecp,y,canvLine,ws,count):
    offset = 0.5*(count-1)*ws
    y += offset
    for idx in xrange(count):
        canvLine(scp, y, ecp, y)
        y -= ws

def _convert2int(value, map, low, high, name, cmd):
    '''private converter tries map(value) low<=int(value)<=high or finally an error'''
    try:
        return map[value]
    except KeyError:
        try:
            ivalue = int(value)
            if low<=ivalue<=high: return ivalue
        except:
            pass
    raise ValueError('Bad %s value %s in %s'%(name,value,str(cmd)))

def _endswith(obj,s):
    try:
        return obj.endswith(s)
    except:
        return 0

def spanFixDim(V0,V,spanCons,lim=None,FUZZ=rl_config._FUZZ):
    #assign required space to variable rows equally to existing calculated values
    M = {}
    if not lim: lim = len(V0)   #in longtables the row calcs may be truncated
    for (x0,x1),v in spanCons.iteritems():
        if x0>=lim: continue
        x1 += 1
        t = sum([V[x]+M.get(x,0) for x in xrange(x0,x1)])
        if t>=v-FUZZ: continue      #already good enough
        X = [x for x in xrange(x0,x1) if V0[x] is None] #variable candidates
        if not X: continue          #something wrong here mate
        v -= t
        v /= float(len(X))
        for x in X:
            M[x] = M.get(x,0)+v
    for x,v in M.iteritems():
        V[x] += v

class _ExpandedCellTuple(tuple):
    pass

class Table(Flowable):
    def __init__(self, data, colWidths=None, rowHeights=None, style=None,
                repeatRows=0, repeatCols=0, splitByRow=1, emptyTableAction=None, ident=None,
                hAlign=None,vAlign=None, normalizedData=0, cellStyles=None):
        self.ident = ident
        self.hAlign = hAlign or 'CENTER'
        self.vAlign = vAlign or 'MIDDLE'
        if not isinstance(data,(tuple,list)):
            raise ValueError("%s invalid data type" % self.identity())
        self._nrows = nrows = len(data)
        self._cellvalues = []
        _seqCW = isinstance(colWidths,(tuple,list))
        _seqRH = isinstance(rowHeights,(tuple,list))
        if nrows: self._ncols = ncols = max(map(_rowLen,data))
        elif colWidths and _seqCW: ncols = len(colWidths)
        else: ncols = 0
        if not emptyTableAction: emptyTableAction = rl_config.emptyTableAction
        self._longTableOptimize = getattr(self,'_longTableOptimize',rl_config.longTableOptimize)
        if not (nrows and ncols):
            if emptyTableAction=='error':
                raise ValueError("%s must have at least a row and column" % self.identity())
            elif emptyTableAction=='indicate':
                self.__class__ = Preformatted
                global _emptyTableStyle
                if '_emptyTableStyle' not in globals().keys():
                    _emptyTableStyle = ParagraphStyle('_emptyTableStyle')
                    _emptyTableStyle.textColor = colors.red
                    _emptyTableStyle.backColor = colors.yellow
                Preformatted.__init__(self,'%s(%d,%d)' % (self.__class__.__name__,nrows,ncols), _emptyTableStyle)
            elif emptyTableAction=='ignore':
                self.__class__ = Spacer
                Spacer.__init__(self,0,0)
            else:
                raise ValueError('%s bad emptyTableAction: "%s"' % (self.identity(),emptyTableAction))
            return

        # we need a cleanup pass to ensure data is strings - non-unicode and non-null
        if normalizedData:
            self._cellvalues = data
        else:
            self._cellvalues = data = self.normalizeData(data)
        if not _seqCW: colWidths = ncols*[colWidths]
        elif len(colWidths)!=ncols:
            if rl_config.allowShortTableRows and isinstance(colWidths,list):
                n = len(colWidths)
                if n<ncols:
                    colWidths[n:] = (ncols-n)*[colWidths[-1]]
                else:
                    colWidths = colWidths[:ncols]
            else:
                raise ValueError("%s data error - %d columns in data but %d in column widths" % (self.identity(),ncols, len(colWidths)))
        if not _seqRH: rowHeights = nrows*[rowHeights]
        elif len(rowHeights) != nrows:
            raise ValueError("%s data error - %d rows in data but %d in row heights" % (self.identity(),nrows, len(rowHeights)))
        for i,d in enumerate(data):
            n = len(d)
            if n!=ncols:
                if rl_config.allowShortTableRows and isinstance(d,list):
                    d[n:] = (ncols-n)*['']
                else:
                    raise ValueError("%s expected %d not %d columns in row %d!" % (self.identity(),ncols,n,i))
        self._rowHeights = self._argH = rowHeights
        self._colWidths = self._argW = colWidths
        if cellStyles is None:
            cellrows = []
            for i in xrange(nrows):
                cellcols = []
                for j in xrange(ncols):
                    cellcols.append(CellStyle(repr((i,j))))
                cellrows.append(cellcols)
            self._cellStyles = cellrows
        else:
            self._cellStyles = cellStyles

        self._bkgrndcmds = []
        self._linecmds = []
        self._spanCmds = []
        self._nosplitCmds = []
        self.repeatRows = repeatRows
        self.repeatCols = repeatCols
        self.splitByRow = splitByRow

        if style:
            self.setStyle(style)

    def __repr__(self):
        "incomplete, but better than nothing"
        r = getattr(self,'_rowHeights','[unknown]')
        c = getattr(self,'_colWidths','[unknown]')
        cv = getattr(self,'_cellvalues','[unknown]')
        import pprint
        cv = pprint.pformat(cv)
        cv = cv.replace("\n", "\n  ")
        return "%s(\n rowHeights=%s,\n colWidths=%s,\n%s\n) # end table" % (self.__class__.__name__,r,c,cv)

    def normalizeData(self, data):
        """Takes a block of input data (list of lists etc.) and
        - coerces unicode strings to non-unicode UTF8
        - coerces nulls to ''
        -

        """
        def normCell(stuff):
            if stuff is None:
                return ''
            elif isinstance(stuff,unicode):
                return stuff.encode('utf8')
            else:
                return stuff
