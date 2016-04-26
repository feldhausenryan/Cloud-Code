# Locale tests: scalar types formatting should be independent of the locale
def in_foreign_locale(func):
    """
    Swap LC_NUMERIC locale to one in which the decimal point is ',' and not '.'
    If not possible, raise nose.SkipTest
    """
    if sys.platform == 'win32':
        locales = ['FRENCH']
    else:
        locales = ['fr_FR', 'fr_FR.UTF-8', 'fi_FI', 'fi_FI.UTF-8']
    def wrapper(*args, **kwargs):
        curloc = locale.getlocale(locale.LC_NUMERIC)
        try:
            for loc in locales:
                try:
                    locale.setlocale(locale.LC_NUMERIC, loc)
                    break
                except locale.Error:
                    pass
            else:
                raise nose.SkipTest("Skipping locale test, because "
                                    "French locale not found")
            return func(*args, **kwargs)
        finally:
            locale.setlocale(locale.LC_NUMERIC, locale=curloc)
    return nose.tools.make_decorator(func)(wrapper)
