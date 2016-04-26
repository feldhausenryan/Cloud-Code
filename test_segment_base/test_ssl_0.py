# Issue #9415: Ubuntu hijacks their OpenSSL and forcefully disables SSLv2
def skip_if_broken_ubuntu_ssl(func):
    if hasattr(ssl, 'PROTOCOL_SSLv2'):
        # We need to access the lower-level wrapper in order to create an
        # implicit SSL context without trying to connect or listen.
        try:
            import _ssl
        except ImportError:
            # The returned function won't get executed, just ignore the error
            pass
        @functools.wraps(func)
        def f(*args, **kwargs):
            try:
                s = socket.socket(socket.AF_INET)
                _ssl.sslwrap(s._sock, 0, None, None,
                             ssl.CERT_NONE, ssl.PROTOCOL_SSLv2, None, None)
            except ssl.SSLError as e:
                if (ssl.OPENSSL_VERSION_INFO == (0, 9, 8, 15, 15) and
                    platform.linux_distribution() == ('debian', 'squeeze/sid', '')
                    and 'Invalid SSL protocol variant specified' in str(e)):
                    raise unittest.SkipTest("Patched Ubuntu OpenSSL breaks behaviour")
            return func(*args, **kwargs)
        return f
    else:
        return func
