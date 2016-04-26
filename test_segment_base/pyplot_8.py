# This function was autogenerated by boilerplate.py.  Do not edit as
# changes will be lost
def hsv():
    '''
    set the default colormap to hsv and apply to current image if any.
    See help(colormaps) for more information
    '''
    rc('image', cmap='hsv')
    im = gci()
    if im is not None:
        im.set_cmap(cm.hsv)
    draw_if_interactive()
