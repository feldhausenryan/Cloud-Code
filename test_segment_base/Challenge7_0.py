#Method One: Fill in from left
#Problem: Runtime is super slow O(x^n) or something worse
def answer(x, y, n):
    if (x + y > n+1):
        return 0
    def x_invalid(x, l):
        count = 0
        track = -1
        for element in l:
            if (element > track):
                count += 1
                track = element
            if (count > x):
                return True
        return False
    def fully_valid(x, y, l):
        l_copy = l[:]
        x_count = 0
        y_count = 0
        x_tracker = -1
        y_tracker = -1
        for value in l_copy:
            if (x_tracker < value):
                x_tracker = value
                x_count += 1
                #save time
                if (x_count > x):
                    return False
        l_copy.reverse()
        for value in l_copy:
            if (y_tracker < value):
                y_tracker = value
                y_count += 1
                #save time
                if (y_count > y):
                    return False
        if (x == x_count and y == y_count):
            return True
        else:
            return False
    def recursive_loop(x, y, n, l, r, v):
        #save time
        if (x_invalid(x, l)):
            return v
        if (r == []):
            if (fully_valid(x, y, l)):
                return v+1
        v_count = v
        for value in r:
            r_copy = r[:]
            r_copy.remove(value)
            l_copy = l[:]
            l_copy.append(value)
            v_count += recursive_loop(x, y, n, l_copy, r_copy, v)
        return v_count + v
    r = [value for value in range(0, n)]
    l = []
    v = 0
    return recursive_loop(x, y, n, l, r, v)
