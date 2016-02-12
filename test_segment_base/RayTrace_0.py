'''
INPUT: A in y=Ax^2 input_a | B and C in y=Bx + C
OUTPUT: The two X coordinates of the intercepts of the parabola.
DISCLAIMER: Does not handle imaginary. Will throw an exception and terminate the program
'''
def getParabolaXIntersection(input_a, input_b, input_c):
    first_x = ((-1)*input_b+pow(pow(input_b, 2) + 4*input_a*input_c, 0.5)) / (-2*input_a)
    second_x = ((-1)*input_b-pow(pow(input_b, 2) + 4*input_a*input_c, 0.5)) / (-2*input_a)
    return (first_x, second_x)

