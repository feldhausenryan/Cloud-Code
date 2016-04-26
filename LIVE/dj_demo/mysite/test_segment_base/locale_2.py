# Strip a given amount of excess padding from the given string
def _strip_padding(s, amount):
    lpos = 0
    while amount and s[lpos] == ' ':
        lpos += 1
        amount -= 1
    rpos = len(s) - 1
    while amount and s[rpos] == ' ':
        rpos -= 1
        amount -= 1
    return s[lpos:rpos+1]
