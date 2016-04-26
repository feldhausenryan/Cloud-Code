# This uses mathtext to render the expression
def latex2png(latex, filename, fontset='cm'):
    latex = "$%s$" % latex
    orig_fontset = rcParams['mathtext.fontset']
    rcParams['mathtext.fontset'] = fontset
    if os.path.exists(filename):
        depth = mathtext_parser.get_depth(latex, dpi=100)
    else:
        try:
            depth = mathtext_parser.to_png(filename, latex, dpi=100)
        except:
            warnings.warn("Could not render math expression %s" % latex,
                          Warning)
            depth = 0
    rcParams['mathtext.fontset'] = orig_fontset
    sys.stdout.write("#")
    sys.stdout.flush()
    return depth
