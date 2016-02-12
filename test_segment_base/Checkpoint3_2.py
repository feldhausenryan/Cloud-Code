'''
# Write this for Checkpoint 3
'''
def count_words( wlist ):
    counts = dict()
    ignoreset = set([item.strip().strip('\n') for item in open('ignore.txt')])
    for word in wlist:
        if word not in ignoreset and word not in counts:
            counts[word] = 1
        elif word not in ignoreset and word in counts:
            counts[word] += 1
    for item in sorted(counts):
        print "%s,%s" %(item,counts[item])
        


