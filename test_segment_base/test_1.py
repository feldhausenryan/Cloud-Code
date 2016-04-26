# Our special command line customization.
# Pre-install hook for our virtual directory.
def PreInstallDirectory(params, options):
    # If the user used our special '--description' option,
    # then we override our default.
    if options.description:
        params.Description = options.description
