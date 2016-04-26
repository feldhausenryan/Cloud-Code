# XXX I suspect this is Unix-specific -- need porting help!
def move_file (src, dst, verbose=1, dry_run=0):
    """Move a file 'src' to 'dst'.
    If 'dst' is a directory, the file will be moved into it with the same
    name; otherwise, 'src' is just renamed to 'dst'.  Return the new
    full name of the file.
    Handles cross-device moves on Unix using 'copy_file()'.  What about
    other systems???
    """
    from os.path import exists, isfile, isdir, basename, dirname
    import errno
    if verbose >= 1:
        log.info("moving %s -> %s", src, dst)
    if dry_run:
        return dst
    if not isfile(src):
        raise DistutilsFileError("can't move '%s': not a regular file" % src)
    if isdir(dst):
        dst = os.path.join(dst, basename(src))
    elif exists(dst):
        raise DistutilsFileError(
              "can't move '%s': destination '%s' already exists" %
              (src, dst))
    if not isdir(dirname(dst)):
        raise DistutilsFileError(
              "can't move '%s': destination '%s' not a valid path" % \
              (src, dst))
    copy_it = 0
    try:
        os.rename(src, dst)
    except os.error, (num, msg):
        if num == errno.EXDEV:
            copy_it = 1
        else:
            raise DistutilsFileError(
                  "couldn't move '%s' to '%s': %s" % (src, dst, msg))
    if copy_it:
        copy_file(src, dst, verbose=verbose)
        try:
            os.unlink(src)
        except os.error, (num, msg):
            try:
                os.unlink(dst)
            except os.error:
                pass
            raise DistutilsFileError(
                  ("couldn't move '%s' to '%s' by copy/delete: " +
                   "delete '%s' failed: %s") %
                  (src, dst, src, msg))
    return dst
