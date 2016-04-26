# This should be quite faster than _matchFormats_orig.
# F. Alted 2006-01-18
def _matchFormats(seq1, seq2):
    """Check if two flat formats lists are equivalent."""
    # Lists must have the same length
    if len(seq1) != len(seq2):
        raise ValueError("""buffer structure doesn't match that """
            """provided by the format specification""")
    # Elements in the same position must describe the same format
    for (f1, f2) in zip(seq1, seq2):
        (repeat1, dtype1) = format_re.match(f1.strip()).groups()
        (repeat2, dtype2) = format_re.match(f2.strip()).groups()
        dtype1 = dtype1.strip()
        dtype2 = dtype2.strip()
        if dtype1 in revfmt: dtype1 = revfmt[dtype1]
        if dtype2 in revfmt: dtype2 = revfmt[dtype2]
        if repeat1 in ['', '1']: dtype1 = '1'+dtype1
        if repeat2 in ['', '1']: dtype2 = '1'+dtype2
        if dtype1 != dtype2:
            raise ValueError("""buffer formats don't match those """
                """provided by the format specification""")
