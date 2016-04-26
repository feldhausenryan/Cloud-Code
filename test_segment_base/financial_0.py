# Use Newton's iteration until the change is less than 1e-6
#  for all values or a maximum of 100 iterations is reached.
#  Newton's rule is
#  r_{n+1} = r_{n} - g(r_n)/g'(r_n)
#     where
#  g(r) is the formula
#  g'(r) is the derivative with respect to r.
def rate(nper, pmt, pv, fv, when='end', guess=0.10, tol=1e-6, maxiter=100):
    """
    Compute the rate of interest per period.
    Parameters
    ----------
    nper : array_like
        Number of compounding periods
    pmt : array_like
        Payment
    pv : array_like
        Present value
    fv : array_like
        Future value
    when : {{'begin', 1}, {'end', 0}}, {string, int}, optional
        When payments are due ('begin' (1) or 'end' (0))
    guess : float, optional
        Starting guess for solving the rate of interest
    tol : float, optional
        Required tolerance for the solution
    maxiter : int, optional
        Maximum iterations in finding the solution
    Notes
    -----
    The rate of interest is computed by iteratively solving the
    (non-linear) equation::
     fv + pv*(1+rate)**nper + pmt*(1+rate*when)/rate * ((1+rate)**nper - 1) = 0
    for ``rate``.
    References
    ----------
    Wheeler, D. A., E. Rathke, and R. Weir (Eds.) (2009, May). Open Document
    Format for Office Applications (OpenDocument)v1.2, Part 2: Recalculated
    Formula (OpenFormula) Format - Annotated Version, Pre-Draft 12.
    Organization for the Advancement of Structured Information Standards
    (OASIS). Billerica, MA, USA. [ODT Document]. Available:
    http://www.oasis-open.org/committees/documents.php?wg_abbrev=office-formula
    OpenDocument-formula-20090508.odt
    """
    when = _convert_when(when)
    nper, pmt, pv, fv, when = map(np.asarray, [nper, pmt, pv, fv, when])
    rn = guess
    iter = 0
    close = False
    while (iter < maxiter) and not close:
        rnp1 = rn - _g_div_gp(rn, nper, pmt, pv, fv, when)
        diff = abs(rnp1-rn)
        close = np.all(diff<tol)
        iter += 1
        rn = rnp1
    if not close:
        # Return nan's in array of the same shape as rn
        return np.nan + rn
    else:
        return rn
