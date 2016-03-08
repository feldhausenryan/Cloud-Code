#Method Two: Fill in order descending ex [2 x x ] then [x 2 x] then [x x 2] before filling in 1
def method_two(x, y, n):
    #Can't see more people than physically possible
    if (x + y > n + 1):
        return 0
    #Can't see less than physically possible
    if (x + y < 3):
        return 0
    t = n
    r = [value for value in range(0, n)]
    l = [-1] * n
    v = 0
    def x_invalid(x, l, n):
        count = 0
        track = -2
        for element in l:
            if (element > track):
                count += 1
                track = element
            if (element == n):
                return False
            if (count > x):
                return True
        return False
    def y_invalid(y, l, n):
        count = 0
        track = -2
        for value in range(len(l)-1, -1, -1):
            if (l[value] > track):
                count += 1
                track = l[value]
            if (l[value] == n):
                return False
            if (count > y):
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
    def recursive_loop(x, y, n, l, r, t, v):
        if (x_invalid(x, l, n-1)):
            return v
        if (y_invalid(y, l, n-1)):
            return v
        if (r == []):
            if (fully_valid(x, y, l)):
                return v + 1
        v_count = 0
        for index in r:
            r_copy = r[:]
            l_copy = l[:]
            r_copy.remove(index)
            l_copy[index] = t
            v_count += recursive_loop(x, y, n, l_copy, r_copy, t-1, v)
        return v_count + v
    #x = x, y = y, n = n, l = growing list, r = remaining index range (helps runtime at expense of memory),
    #t = tracker for next value to fill into l, v = sum of valid results    
    return recursive_loop(x, y, n, l, r, t, v)
