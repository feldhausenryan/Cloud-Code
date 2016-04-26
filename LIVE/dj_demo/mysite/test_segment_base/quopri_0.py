# Other helper functions
def ishex(c):
    """Return true if the character 'c' is a hexadecimal digit."""
    return '0' <= c <= '9' or 'a' <= c <= 'f' or 'A' <= c <= 'F'
