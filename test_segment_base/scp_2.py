# functions related to the command-line interface
def log(level, msg, *args):
    if verbose >= level:
        print msg % args
