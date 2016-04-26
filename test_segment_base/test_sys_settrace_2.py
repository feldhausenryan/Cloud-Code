# check that lines consisting of just one instruction get traced:
def one_instr_line():
    x = 1
    del x
    x = 1
