'''
#INPUT: An input slope and an x value of the parabola
OUTPUT: The slope of the reflected line
DISCLAIMER: Will not handle a slope of Infinity. The program will throw an exception and terminate
'''
def getSlopeFromReflection(input_slope, parabola_x):
    temp = -4*pow(parabola_x, 2)*input_slope - 4*parabola_x + input_slope
    temp2 = 4*pow(parabola_x, 2) - 4*input_slope*parabola_x - 1
    return temp / temp2

