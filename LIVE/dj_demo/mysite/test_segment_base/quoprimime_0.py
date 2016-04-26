# Helpers
def header_quopri_check(c):
    """Return True if the character should be escaped with header quopri."""
    return bool(hqre.match(c))
