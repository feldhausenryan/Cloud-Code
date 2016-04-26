# helper functions
def fixasctime(s):
    if s[8] == ' ':
        s = s[:8] + '0' + s[9:]
    return s
