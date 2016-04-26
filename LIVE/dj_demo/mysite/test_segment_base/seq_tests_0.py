# Various iterables
# This is used for checking the constructor (here and in test_deque.py)
def iterfunc(seqn):
    'Regular generator'
    for i in seqn:
        yield i
