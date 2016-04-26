# Split a string in "words" according to findwordend
def splitwords(str, minlength):
    words = []
    i = 0
    n = len(str)
    while i < n:
        while i < n and str[i] in ' \t\n': i = i+1
        if i >= n: break
        start = i
        i = findwordend(str, i, n)
        words.append(str[start:i])
    while len(words) < minlength: words.append('')
    return words
