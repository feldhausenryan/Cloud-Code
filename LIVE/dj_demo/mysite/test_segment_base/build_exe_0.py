# XXX Perhaps it would be better to assume dlls from the systemdir are system dlls,
# and make some exceptions for known dlls, like msvcr71, pythonXY.dll, and so on?
def isSystemDLL(pathname):
    if os.path.basename(pathname).lower() in ("msvcr71.dll", "msvcr71d.dll"):
        return 0
    if os.path.basename(pathname).lower() in EXCLUDED_DLLS:
        return 1
    # How can we determine whether a dll is a 'SYSTEM DLL'?
    # Is it sufficient to use the Image Load Address?
    import struct
    file = open(pathname, "rb")
    if file.read(2) != "MZ":
        raise Exception, "Seems not to be an exe-file"
    file.seek(0x3C)
    pe_ofs = struct.unpack("i", file.read(4))[0]
    file.seek(pe_ofs)
    if file.read(4) != "PE\000\000":
        raise Exception, ("Seems not to be an exe-file", pathname)
    file.read(20 + 28) # COFF File Header, offset of ImageBase in Optional Header
    imagebase = struct.unpack("I", file.read(4))[0]
    return not (imagebase < 0x70000000)
