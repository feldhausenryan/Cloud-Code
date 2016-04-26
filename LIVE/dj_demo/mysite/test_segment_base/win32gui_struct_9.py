# Generic function for packing a DEV_BROADCAST_* structure - generally used
# by the other PackDEV_BROADCAST_* functions in this module.
def PackDEV_BROADCAST(devicetype, rest_fmt, rest_data, extra_data=_make_bytes('')):
    # It seems a requirement is 4 byte alignment, even for the 'BYTE data[1]'
    # field (eg, that would make DEV_BROADCAST_HANDLE 41 bytes, but we must
    # be 44.
    extra_data += _make_bytes('\0' * (4-len(extra_data)%4))
    format = "iii" + rest_fmt
    full_size = struct.calcsize(format) + len(extra_data)
    data = (full_size, devicetype, 0) + rest_data
    return struct.pack(format, *data) + extra_data
