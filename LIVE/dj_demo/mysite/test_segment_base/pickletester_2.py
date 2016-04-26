# Return the number of times opcode code appears in pickle.
def count_opcode(code, pickle):
    n = 0
    for op, dummy, dummy in pickletools.genops(pickle):
        if op.code == code:
            n += 1
    return n
