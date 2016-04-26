# Return machine address `a` as a (possibly long) non-negative integer.
# Starting with Python 2.5, id(anything) is always non-negative, and
# the ctypes addressof() inherits that via PyLong_FromVoidPtr().
def positive_address(a):
    if a >= 0:
        return a
    # View the bits in `a` as unsigned instead.
    import struct
    num_bits = struct.calcsize("P") * 8 # num bits in native machine address
    a += 1L << num_bits
    assert a >= 0
    return a
