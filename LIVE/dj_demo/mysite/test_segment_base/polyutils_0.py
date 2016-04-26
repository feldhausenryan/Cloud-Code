#
# Helper functions to convert inputs to 1-D arrays
#
def trimseq(seq) :
    """Remove small Poly series coefficients.
    Parameters
    ----------
    seq : sequence
        Sequence of Poly series coefficients. This routine fails for
        empty sequences.
    Returns
    -------
    series : sequence
        Subsequence with trailing zeros removed. If the resulting sequence
        would be empty, return the first element. The returned sequence may
        or may not be a view.
    Notes
    -----
    Do not lose the type info if the sequence contains unknown objects.
    """
    if len(seq) == 0 :
        return seq
    else :
        for i in range(len(seq) - 1, -1, -1) :
            if seq[i] != 0 :
                break
        return seq[:i+1]
