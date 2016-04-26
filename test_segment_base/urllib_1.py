# Test and time quote() and unquote()
def test1():
    s = ''
    for i in range(256): s = s + chr(i)
    s = s*4
    t0 = time.time()
    qs = quote(s)
    uqs = unquote(qs)
    t1 = time.time()
    if uqs != s:
        print 'Wrong!'
    print repr(s)
    print repr(qs)
    print repr(uqs)
    print round(t1 - t0, 3), 'sec'
