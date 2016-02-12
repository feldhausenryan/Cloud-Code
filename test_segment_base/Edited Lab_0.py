'''
Function to determine if a string contains three consecutive double lectures
 It has been switched slightly to use a for loop instead of a while loop.
'''
def three_double(s):
    for i in range(0, len(s)-3):
        if s[i] == s[i+1] and s[i+2] == s[i+3]:
            return True
    return False

