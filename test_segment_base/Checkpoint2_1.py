# Write this for Checkpoint 2
def find_words( rstring ):
    rstring = rstring.strip()
    rstring = rstring.replace("\t"," ")
    rstring = rstring.replace("\n"," ")
    rstring = rstring.lower()
    i=0
    r2 = rstring
    Ignored = False
    word = ""
    while i<len(r2):
        if r2[i] in "abcdefghijklmnopqrstuvwxyz":
            word += r2[i]
        elif r2[i] in "&" and len(word)<>0:
            print word
            word = ""
            Ignored = True
        elif r2[i] in "&" and len(word)==0:
            Ignored = True
        elif r2[i] in " " and not Ignored and len(word)<>0:
            print word
            word = ""
        elif r2[i] in " " and Ignored:
            Ignored = False
            word = ""
        i +=1
