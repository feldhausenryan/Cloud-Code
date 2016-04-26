'''
from UserDict import UserDict
from reportlab.lib.validators import isAnything, _SequenceTypes, DerivedValue
from reportlab import rl_config

class CallableValue:
    '''a class to allow callable initial values'''
    def __init__(self,func,*args,**kw):
        #assert iscallable(func)
        self.func = func
        self.args = args
        self.kw = kw
