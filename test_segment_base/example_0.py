# A function to minimize
# Must return a tuple with the function value and the value of the constraints
# or None to abort the minimization
def function(x):
        f = x[0]**2+abs(x[1])**3
        # Two constraints to represent the equality constraint x**2+y**2 == 25
        con = [0]*2
        con[0] = x[0]**2 + x[1]**2 - 25 # x**2+y**2 >= 25
        con[1] = - con[0] # x**2+y**2 <= 25
        return f, con
