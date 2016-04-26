##################################################################
#                       FUNCTION OPCODIZE                        #
##################################################################
def opcodize(s):
    "Slightly more readable form"
    length = len(s)
    i = 0
    answer = []
    while i < length:
        bytecode = ord(s[i])
        name = byOpcode[bytecode]
        if bytecode >= haveArgument:
            argument = 256*ord(s[i+2])+ord(s[i+1])
            i += 3
        else:
            argument = None
            i += 1
        answer.append((bytecode,argument,name))
    return answer
