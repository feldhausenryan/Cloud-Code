# This function was autogenerated by boilerplate.py.  Do not edit as
# changes will be lost
def pink():
    '''
    set the default colormap to pink and apply to current image if any.
    See help(colormaps) for more information
    '''
    rc('image', cmap='pink')
    im = gci()
    if im is not None:
        im.set_cmap(cm.pink)
    draw_if_interactive()