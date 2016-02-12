'''
Write this for Checkpoint 1
'''
def remove_inbetween( in_s, c0, c1):
    countxxx = 0    
    while in_s.find(c0)<>-1 and in_s.find(c1)<>-1:
        in_s = in_s[:in_s.find(c0)]+in_s[in_s.find(c1)+1:]
        countxxx+=1
        print len(in_s) if countxxx <>53 else in_s
        print countxxx
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
    '''
    return in_s
        


