# Write this for Checkpoint 1
def remove_inbetween( in_s, c0, c1):
    '''
    while in_s.find(c0)<>-1:
        in_s = in_s[:in_s.find(c0)]+in_s[in_s.find(c1)+1:]
    '''
    goodletter = True
    new = ""
    for letter in in_s:
        if letter == c0:
            goodletter = False
        if goodletter:
            new += letter 
        if letter == c1:
            goodletter = True
    return new
