# This function was autogenerated by boilerplate.py.  Do not edit as
# changes will be lost
def gray():
    '''
    set the default colormap to gray and apply to current image if any.
    See help(colormaps) for more information
    '''
    rc('image', cmap='gray')
    im = gci()
    if im is not None:
        im.set_cmap(cm.gray)
    draw_if_interactive()