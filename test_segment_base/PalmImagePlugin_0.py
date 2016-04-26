# so build a prototype image to be used for palette resampling
def build_prototype_image():
    image = Image.new("L", (1,len(_Palm8BitColormapValues),))
    image.putdata(list(range(len(_Palm8BitColormapValues))))
    palettedata = ()
    for i in range(len(_Palm8BitColormapValues)):
        palettedata = palettedata + _Palm8BitColormapValues[i]
    for i in range(256 - len(_Palm8BitColormapValues)):
        palettedata = palettedata + (0, 0, 0)
    image.putpalette(palettedata)
    return image
