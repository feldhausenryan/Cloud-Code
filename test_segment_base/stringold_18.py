# Center a string
def center(s, width):
    """center(s, width) -> string
    Return a center version of s, in a field of the specified
    width. padded with spaces as needed.  The string is never
    truncated.
    """
    n = width - len(s)
    if n <= 0: return s
    half = n/2
    if n%2 and width%2:
        # This ensures that center(center(s, i), j) = center(s, j)
        half = half+1
    return ' '*half +  s + ' '*(n-half)
