# get_bbox is deprecated. I don't see any reason to use ghostscript to
# find the bounding box, as the required bounding box is alread known.
def get_bbox(tmpfile, bbox):
    """
    Use ghostscript's bbox device to find the center of the bounding box. Return
    an appropriately sized bbox centered around that point. A bit of a hack.
    """
    outfile = tmpfile + '.output'
    if sys.platform == 'win32': gs_exe = 'gswin32c'
    else: gs_exe = 'gs'
    command = '%s -dBATCH -dNOPAUSE -sDEVICE=bbox "%s"' %\
                (gs_exe, tmpfile)
    verbose.report(command, 'debug')
    stdin, stdout, stderr = os.popen3(command)
    verbose.report(stdout.read(), 'debug-annoying')
    bbox_info = stderr.read()
    verbose.report(bbox_info, 'helpful')
    bbox_found = re.search('%%HiResBoundingBox: .*', bbox_info)
    if bbox_found:
        bbox_info = bbox_found.group()
    else:
        raise RuntimeError('Ghostscript was not able to extract a bounding box.\
