# TODO: Vectorize this
def autocontrast(image, cutoff=0):
    """
    Maximize image contrast, based on histogram.  This completely
    ignores the alpha channel.
    """
    assert image.dtype == np.uint8
    output_image = np.empty((image.shape[0], image.shape[1], 3), np.uint8)
    for i in xrange(0, 3):
        plane = image[:,:,i]
        output_plane = output_image[:,:,i]
        h = np.histogram(plane, bins=256)[0]
        if cutoff:
            # cut off pixels from both ends of the histogram
            # get number of pixels
            n = 0
            for ix in xrange(256):
                n = n + h[ix]
            # remove cutoff% pixels from the low end
            cut = n * cutoff / 100
            for lo in range(256):
                if cut > h[lo]:
                    cut = cut - h[lo]
                    h[lo] = 0
                else:
                    h[lo] = h[lo] - cut
                    cut = 0
                if cut <= 0:
                    break
            # remove cutoff% samples from the hi end
            cut = n * cutoff / 100
            for hi in xrange(255, -1, -1):
                if cut > h[hi]:
                    cut = cut - h[hi]
                    h[hi] = 0
                else:
                    h[hi] = h[hi] - cut
                    cut = 0
                if cut <= 0:
                    break
        # find lowest/highest samples after preprocessing
        for lo in xrange(256):
            if h[lo]:
                break
        for hi in xrange(255, -1, -1):
            if h[hi]:
                break
        if hi <= lo:
            output_plane[:,:] = plane
        else:
            scale = 255.0 / (hi - lo)
            offset = -lo * scale
            lut = np.arange(256, dtype=np.float)
            lut *= scale
            lut += offset
            lut = lut.clip(0, 255)
            lut = lut.astype(np.uint8)
            output_plane[:,:] = lut[plane]
    return output_image
