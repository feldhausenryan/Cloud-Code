######################################################################
# Useful functions.
######################################################################
def setup_logger(logger, fname, stream=True, mode=logging.ERROR):
    """Setup a log file and the logger.  If the given file name is not
    absolute, put the log file in `ETSConfig.application_home`, if not
    it will create it where desired.
    Parameters:
    -----------
    fname -- file name the logger should use.  If this is an absolute
    path it will create the log file as specified, if not it will put it
    in `ETSConfig.application_home`.
    stream -- Add a stream handler.
    mode -- the logging mode of the stream handler.
    """
    if not os.path.isabs(fname):
        path = os.path.join(ETSConfig.application_home, fname)
    else:
        path = fname
    # Check if we have already added a logger (can happen when the app
    # is started multiple number of times from ipython say).
    handlers = logger.handlers
    if len(handlers) > 1:
        h = handlers[0]
        if isinstance(h, LogFileHandler) and h.baseFilename == path:
            logger.info('Logging handlers already set!  Not duplicating.')
            return
    logger.setLevel(logging.DEBUG)
    handler = LogFileHandler(path)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    if stream:
        s = logging.StreamHandler()
        s.setFormatter(FORMATTER)
        s.setLevel(mode)
        logger.addHandler(s)
    logger.info("*"*80)
    logger.info("logfile is: '%s'", os.path.abspath(path))
    logger.info("*"*80)
