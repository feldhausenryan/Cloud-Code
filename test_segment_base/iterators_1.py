# These two functions are imported into the Iterators.py interface module.
def body_line_iterator(msg, decode=False):
    """Iterate over the parts, returning string payloads line-by-line.
    Optional decode (default False) is passed through to .get_payload().
    """
    for subpart in msg.walk():
        payload = subpart.get_payload(decode=decode)
        if isinstance(payload, basestring):
            for line in StringIO(payload):
                yield line
