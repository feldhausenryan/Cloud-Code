"""
import string, sys, os, re

class Formatter:
    "Base formatter - simply applies python format strings"
    def __init__(self, pattern):
        self.pattern = pattern
    def format(self, obj):
        return self.pattern % obj
    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.pattern)
    def __call__(self, x):
        return self.format(x)


_ld_re=re.compile(r'^\d*\.')
_tz_re=re.compile('0+$')
class DecimalFormatter(Formatter):
    """lets you specify how to build a decimal.

    A future NumberFormatter class will take Microsoft-style patterns
    instead - "$#,##0.00" is WAY easier than this."""
    def __init__(self, places=2, decimalSep='.', thousandSep=None, prefix=None, suffix=None):
        if places=='auto':
            self.calcPlaces = self._calcPlaces
        else:
            self.places = places
        self.dot = decimalSep
        self.comma = thousandSep
        self.prefix = prefix
        self.suffix = suffix
