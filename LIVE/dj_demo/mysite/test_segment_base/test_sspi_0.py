# It is quite likely that the Kerberos tests will fail due to not being
# installed.  The NTLM tests do *not* get the same behaviour as they should
# always be there.
def applyHandlingSkips(func, *args):
    try:
        return func(*args)
    except win32api.error, exc:
        if exc.winerror == sspicon.SEC_E_NO_CREDENTIALS:
            raise TestSkipped(exc)
        raise
