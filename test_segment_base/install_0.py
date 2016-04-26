# Convert an ADSI COM exception to the Win32 error code embedded in it.
def _GetWin32ErrorCode(com_exc):
    hr = com_exc.hresult
    # If we have more details in the 'excepinfo' struct, use it.
    if com_exc.excepinfo:
        hr = com_exc.excepinfo[-1]
    if winerror.HRESULT_FACILITY(hr) != winerror.FACILITY_WIN32:
        raise
    return winerror.SCODE_CODE(hr)
