# This function was autogenerated by boilerplate.py.  Do not edit as
# changes will be lost
def hot():
    '''
    set the default colormap to hot and apply to current image if any.
    See help(colormaps) for more information
    '''
    rc('image', cmap='hot')
    im = gci()
    if im is not None:
        im.set_cmap(cm.hot)
    draw_if_interactive()
