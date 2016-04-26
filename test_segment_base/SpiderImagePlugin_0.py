# given a list of filenames, return a list of images
def loadImageSeries(filelist=None):
    " create a list of Image.images for use in montage "
    if filelist == None or len(filelist) < 1:
        return
    imglist = []
    for img in filelist:
        if not os.path.exists(img):
            print("unable to find %s" % img)
            continue
        try:
            im = Image.open(img).convert2byte()
        except:
            if not isSpiderImage(img):
                print(img + " is not a Spider image file")
            continue
        im.info['filename'] = img
        imglist.append(im)
    return imglist
