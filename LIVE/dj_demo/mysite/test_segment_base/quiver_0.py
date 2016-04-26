# This is a helper function that parses out the various combination of
# arguments for doing colored vector plots.  Pulling it out here
# allows both Quiver and Barbs to use it
def _parse_args(*args):
    X, Y, U, V, C = [None]*5
    args = list(args)
    # The use of atleast_1d allows for handling scalar arguments while also
    # keeping masked arrays
    if len(args) == 3 or len(args) == 5:
        C = np.atleast_1d(args.pop(-1))
    V = np.atleast_1d(args.pop(-1))
    U = np.atleast_1d(args.pop(-1))
    if U.ndim == 1:
        nr, nc = 1, U.shape[0]
    else:
        nr, nc = U.shape
    if len(args) == 2: # remaining after removing U,V,C
        X, Y = [np.array(a).ravel() for a in args]
        if len(X) == nc and len(Y) == nr:
            X, Y = [a.ravel() for a in np.meshgrid(X, Y)]
    else:
        indexgrid = np.meshgrid(np.arange(nc), np.arange(nr))
        X, Y = [np.ravel(a) for a in indexgrid]
    return X, Y, U, V, C
