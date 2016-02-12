'''
# Function to apply the three_double test to each string in the words
 list.  It counts the number of results.
'''
def find_three_double(words_list):
    count = 0
    for w in words_list:
        if three_double(w):
            print w
            count = count + 1
    if count == 0:
        print '<None found>'
    else:
        print count, 'found'

