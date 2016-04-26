# Check that the 2 objects both have identical COM pointers.
def CheckSameCOMObject(ob1, ob2):
    addr1 = repr(ob1).split()[6][:-1]
    addr2 = repr(ob2).split()[6][:-1]
    return addr1==addr2
