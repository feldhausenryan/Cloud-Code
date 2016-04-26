# implicit return example
# This test is interesting because of the else: pass
# part of the code.  The code generate for the true
# part of the if contains a jump past the else branch.
# The compiler then generates an implicit "return None"
# Internally, the compiler visits the pass statement
# and stores its line number for use on the next instruction.
# The next instruction is the implicit return None.
def ireturn_example():
    a = 5
    b = 5
    if a == b:
        b = a+1
    else:
        pass
