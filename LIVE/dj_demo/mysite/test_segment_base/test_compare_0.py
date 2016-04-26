# Needed for python 3. "cmp" vanished in 3.0.1
def cmp(a, b) :
    if a==b : return 0
    if a<b : return -1
    return 1
