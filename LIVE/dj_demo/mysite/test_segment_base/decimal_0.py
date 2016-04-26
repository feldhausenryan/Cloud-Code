# This function from Tim Peters was taken from here:
# http://mail.python.org/pipermail/python-list/1999-July/007758.html
# The correction being in the function definition is for speed, and
# the whole function is not resolved with math.log because of avoiding
# the use of floats.
def _nbits(n, correction = {
        '0': 4, '1': 3, '2': 2, '3': 2,
        '4': 1, '5': 1, '6': 1, '7': 1,
        '8': 0, '9': 0, 'a': 0, 'b': 0,
        'c': 0, 'd': 0, 'e': 0, 'f': 0}):
    """Number of bits in binary representation of the positive integer n,
    or 0 if n == 0.
    """
    if n < 0:
        raise ValueError("The argument to _nbits should be nonnegative.")
    hex_n = "%x" % n
    return 4*len(hex_n) - correction[hex_n[0]]
