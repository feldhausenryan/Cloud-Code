"""

import string
from reportlab.pdfgen import pdfgeom
from reportlab.lib.utils import fp_str


class PDFPathObject:
    """Represents a graphic path.  There are certain 'modes' to PDF
    drawing, and making a separate object to expose Path operations
    ensures they are completed with no run-time overhead.  Ask
    the Canvas for a PDFPath with getNewPathObject(); moveto/lineto/
    curveto wherever you want; add whole shapes; and then add it back
    into the canvas with one of the relevant operators.

    Path objects are probably not long, so we pack onto one line

    the code argument allows a canvas to get the operatiosn appended directly so
    avoiding the final getCode
    """
    def __init__(self,code=None):
        self._code = (code,[])[code is None]
        self._code_append = self._init_code_append
