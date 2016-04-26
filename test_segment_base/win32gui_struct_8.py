# List view hit-test.
def PackLVHITTEST(pt):
    format = "iiiii"
    buf = struct.pack(format,
                      pt[0], pt[1],
                      0, 0, 0)
    return array.array("b", buf), None
