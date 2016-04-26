"""Selection-buffer handling code

This code is resonsible for turning gluint *
arrays into structured representations for use
by Python-level code.
"""
def uintToLong( value ):
    if value < 0:
        # array type without a uint, so represented as an int 
        value = (value & 0x7fffffff) + 0x80000000
    return value
