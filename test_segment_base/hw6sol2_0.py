'''
#These Functions are copied from checkpoint 3 of Lab 9 (Used for better functionality)"
def remove_inbetween( in_s, c0, c1):
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
def strip_html(in_s):
    result = remove_inbetween( in_s, '<', '>' )
    result = remove_inbetween( result, '{', '}' )
    return result
def find_words( rstring ):
    rstring = rstring.strip()
    rstring = rstring.replace("\t"," ")
    rstring = rstring.replace("\n"," ")
    rstring = rstring.lower()
    i=0
    r2 = rstring
    Ignored = False
    word = ""
    wordlist = []
    while i<len(r2):
        if r2[i] in "abcdefghijklmnopqrstuvwxyz":
            word += r2[i]
        elif r2[i] in "&" and len(word)<>0:
            wordlist.append(word)
            word = ""
            Ignored = True
        elif r2[i] in "&" and len(word)==0:
            Ignored = True
        elif r2[i] in " " and not Ignored and len(word)<>0:
            wordlist.append(word)
            word = ""
        elif r2[i] in " " and Ignored:
            Ignored = False
            word = ""
        i +=1
    return wordlist
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
#End of Lab9 functions
'''       
def is_word_in_page(url,word):
    wordlist = check2.find_words(check2.strip_html(urllib.urlopen(url).read()))
    return True if word in wordlist else False
def short_word_list(url):
    wordlist = check2.find_words(check2.strip_html(urllib.urlopen(url).read()))
    ignoreset = set([item.strip().strip('\n') for item in open('ignore.txt')])
    shortwordlist = []
    for word in wordlist:
        if word not in ignoreset and len(word) > 3:
           shortwordlist.append(word)
    return shortwordlist
'''
def short_word_list(url):
    wordlist = find_words(strip_html(urllib.urlopen(url).read()))
    ignoreset = set([item.strip().strip('\n') for item in open('ignore.txt')])
    shortwordlist = []
    for word in wordlist:
        if word not in ignoreset and len(word) > 3:
           shortwordlist.append(word)
    return shortwordlist
