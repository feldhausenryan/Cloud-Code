# vi standalone functions
def vi_is_word (char):
    log ('xx vi_is_word: type(%s), %s' % (type(char), char, ))
    return char.isalpha() or char.isdigit() or char == '_'
