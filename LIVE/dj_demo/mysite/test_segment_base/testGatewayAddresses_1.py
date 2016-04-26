# Check that the objects conform to COM identity rules.
def CheckObjectIdentity(ob1, ob2):
    u1 = ob1.QueryInterface(pythoncom.IID_IUnknown)
    u2 = ob2.QueryInterface(pythoncom.IID_IUnknown)
    return CheckSameCOMObject(u1, u2)
