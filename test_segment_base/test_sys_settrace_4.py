# Tight loop with while(1) example (SF #765624)
def tightloop_example():
    items = range(0, 3)
    try:
        i = 0
        while 1:
            b = items[i]; i+=1
    except IndexError:
        pass
