'''
#INPUT: An input line y = Bx + C and a horizontal line of height F
OUTPUT: The X value of the intersection of the two lines
'''
def getCapXIntersection(input_b, input_c, input_f):
    temp = (input_f-input_c) / input_b
    return temp

