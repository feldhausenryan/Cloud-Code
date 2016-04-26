## Callback function invoked when header data is ready
def header(buf):
    # Print header data to stderr
    sys.stderr.write(buf)
