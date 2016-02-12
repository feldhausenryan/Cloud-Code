'''
# Function to read and apply the three_double test to each string in
 an input file.  It counts the number of results.
'''
def find_three_double(fin):
    count = 0
    for w in fin:
        w = w.strip().strip('\n')
        if three_double(w):
            print w
            count = count + 1
    if count == 0:
        print '<None found>'
    else:
        print count, 'found'

