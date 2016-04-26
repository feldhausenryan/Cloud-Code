# Send a simple "message" over a socket - send the number of bytes first,
# then the string.  Ditto for receive.
def _send_msg(s, m):
    s.send(struct.pack("i", len(m)))
    s.send(m)
