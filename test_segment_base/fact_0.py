'''
This version prints intermediate results from the factorial calculation
 using indentation to show the level of recursion.
'''
def fact(n):
    print ".."*n, n
    if n == 0:
        print "returning 1"
        return 1
    else:
        result = fact(n-1)
        print ".."*n, "result %d" %result
        return n * result

