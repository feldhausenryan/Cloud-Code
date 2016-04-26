#==============================================================================
# Generic image read/write functions
#==============================================================================
def imread(fname, ext=None, to_grayscale=False):
    """Return a NumPy array from an image filename `fname`.
    If `to_grayscale` is True, convert RGB images to grayscale
    The `ext` (optional) argument is a string that specifies the file extension
    which defines the input format: when not specified, the input format is 
    guessed from filename."""
    if not is_text_string(fname):
        fname = to_text_string(fname) # in case filename is a QString instance
    if ext is None:
        _base, ext = osp.splitext(fname)
    arr = iohandler.get_readfunc(ext)(fname)
    if to_grayscale and arr.ndim == 3:
        # Converting to grayscale
        return arr[..., :4].mean(axis=2)
    else:
        return arr
