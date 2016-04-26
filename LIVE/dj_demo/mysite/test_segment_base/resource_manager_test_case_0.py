# mimics urllib2.urlopen for some tests.
# In setUp it replaces urllib2.urlopen for some tests,
# and in tearDown, the regular urlopen is put back into place.
def stubout_urlopen(url):
    if 'bogus' in url:
        raise urllib2.HTTPError(url, '404', 'No such resource', '', None)
    elif 'localhost' in url:
        return StringIO.StringIO('This is a test file.\n')
    else:
        raise ValueError('Unexpected URL %r in stubout_urlopen' % url)
