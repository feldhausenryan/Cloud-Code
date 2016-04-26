# Admire!
def testPlot():
    if 'np' not in dir():
        import PyQt4.Qwt5.anynumpy as np
    x = np.arange(-2*np.pi, 2*np.pi, 0.01)
    p = Plot(Axis(Bottom, "linear x-axis"),
             Axis(Left, "linear y-axis"),
             Axis(Right, Log, "logarithmic y-axis"),             
             Curve(x, np.cos(x), Pen(Magenta, 2), "cos(x)"),
             Curve(x, np.exp(x), Pen(Red), "exp(x)", Right),
             "PyQwt using Qt-%s and Qwt-%s" % (QT_VERSION_STR, QWT_VERSION_STR),
             )
    x = x[0:-1:10]
    p.plot(
        Curve(x, np.cos(x-np.pi/4), Symbol(Circle, Yellow), "circle"),
        Curve(x, np.cos(x+np.pi/4), Pen(Blue), Symbol(Square, Cyan), "square"),
        )
    return p
