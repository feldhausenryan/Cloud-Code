#==============================================================================
# Deprecated functions
#==============================================================================
def imagefile_to_array(filename, to_grayscale=False):
    """
    Return a NumPy array from an image file `filename`
    If `to_grayscale` is True, convert RGB images to grayscale
    """
    print("io.imagefile_to_array is deprecated: use io.imread instead", file=sys.stderr)
    return imread(filename, to_grayscale=to_grayscale)
