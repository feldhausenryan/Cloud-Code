# Replace characters that aren't perfectly safe by dashes
# Underscores are bad since Cern HTTPD treats them as delimiters for
# encoding times, so you get mismatches if you compress your files:
# a.html.gz will map to a_b.html.gz
def fixfunnychars(addr):
    i = 0
    while i < len(addr):
        c = addr[i]
        if c not in goodchars:
            c = '-'
            addr = addr[:i] + c + addr[i+1:]
        i = i + len(c)
    return addr
