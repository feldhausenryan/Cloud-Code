# XXX use python datetime
def check_date(option, opt, value):
    """check a file value
    return the filepath
    """
    try:
        return DateTime.strptime(value, "%Y/%m/%d")
    except DateTime.Error :
        raise OptionValueError(
            "expected format of %s is yyyy/mm/dd" % opt)
