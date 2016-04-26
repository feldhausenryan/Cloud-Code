# Increment a string used as an enumeration
def increment(s):
    if not s:
        return '1'
    for sequence in string.digits, string.lowercase, string.uppercase:
        lastc = s[-1]
        if lastc in sequence:
            i = sequence.index(lastc) + 1
            if i >= len(sequence):
                if len(s) == 1:
                    s = sequence[0]*2
                    if s == '00':
                        s = '10'
                else:
                    s = increment(s[:-1]) + sequence[0]
            else:
                s = s[:-1] + sequence[i]
            return s
    return s # Don't increment
