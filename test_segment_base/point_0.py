# functions for plotting error bars
# different styles are made up of combinations of these functions
# each function takes the same arguments
def _errorBarsBar(style, xmin, xmax, ymin, ymax, xplotter, yplotter,
                  s, painter, clip):
    """Draw bar style error lines."""
    # vertical error bars
    if ymin is not None and ymax is not None and not s.ErrorBarLine.hideVert:
        utils.plotLinesToPainter(painter, xplotter, ymin, xplotter, ymax, clip)
    # horizontal error bars
    if xmin is not None and xmax is not None and not s.ErrorBarLine.hideHorz:
        utils.plotLinesToPainter(painter, xmin, yplotter, xmax, yplotter, clip)
