# Convert a string to ASCII upper case irrespective of the current locale.
def ascii_upper(s):
    return s.translate(_ascii_trans_table)
