# Helpers
def base64_len(s):
    """Return the length of s when it is encoded with base64."""
    groups_of_3, leftover = divmod(len(s), 3)
    # 4 bytes out for each 3 bytes (or nonzero fraction thereof) in.
    # Thanks, Tim!
    n = groups_of_3 * 4
    if leftover:
        n += 4
    return n
