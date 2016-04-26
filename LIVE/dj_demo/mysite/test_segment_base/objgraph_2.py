# Return a flattened version of a list of strings: the concatenation
# of its elements with intervening spaces.
#
def flat(list):
    s = ''
    for item in list:
        s = s + ' ' + item
    return s[1:]
