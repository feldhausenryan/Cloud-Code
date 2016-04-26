# Return True if opcode code appears in the pickle, else False.
def opcode_in_pickle(code, pickle):
    for op, dummy, dummy in pickletools.genops(pickle):
        if op.code == code:
            return True
    return False
